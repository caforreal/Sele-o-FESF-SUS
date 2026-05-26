
import subprocess
import re


def ping_device(ip):

    try:

        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            capture_output=True,
            text=True
        )

        output = result.stdout

        if result.returncode == 0:

            match = re.search(r"time=(\d+\.?\d*)", output)

            latency = match.group(1) + " ms" if match else "?"

            return {
                "status": "online",
                "latency": latency
            }

        return {
            "status": "offline",
            "latency": "timeout"
        }

    except Exception:

        return {
            "status": "unknown",
            "latency": "?"
        }


def get_device_status(device):
    from .models import DeviceMonitor

    try:

        ip = device.primary_ip4

        if not ip:

            result = {
                "status": "unknown",
                "latency": "?"
            }

        else:

            ip_str = str(ip.address).split("/")[0]

            result = ping_device(ip_str)

        DeviceMonitor.objects.update_or_create(
            device=device,
            defaults={
                "status": result["status"],
                "latency": result["latency"]
            }
        )

        return result

    except Exception:

        return {
            "status": "unknown",
            "latency": "?"
        }