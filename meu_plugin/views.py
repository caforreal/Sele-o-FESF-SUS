from django.shortcuts import render

from dcim.models import Device

from .tables import DeviceMonitorTable

from .models import DeviceMonitor


def monitor_view(request):

    query = request.GET.get("q")

    devices = Device.objects.all()

    if query:

        devices = devices.filter(
            name__icontains=query
        )

    table = DeviceMonitorTable(devices)

    online_count = DeviceMonitor.objects.filter(
        status="online"
    ).count()

    offline_count = DeviceMonitor.objects.filter(
        status="offline"
    ).count()

    unknown_count = DeviceMonitor.objects.filter(
        status="unknown"
    ).count()

    monitors = DeviceMonitor.objects.all()

    latencies = []

    for monitor in monitors:

        try:

            value = float(
                monitor.latency.replace(" ms", "")
            )

            latencies.append(value)

        except Exception:
            pass

    avg_latency = (
        round(sum(latencies) / len(latencies), 1)
        if latencies else 0
    )

    return render(
        request,
        "meu_plugin/home.html",
        {
            "table": table,

            "online_count": online_count,

            "offline_count": offline_count,

            "unknown_count": unknown_count,

            "avg_latency": avg_latency,
        }
    )