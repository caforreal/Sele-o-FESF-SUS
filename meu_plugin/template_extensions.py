from django.template.loader import render_to_string
from netbox.plugins import PluginTemplateExtension

from .utils import get_device_status


class DeviceStatusExtension(PluginTemplateExtension):

    model = "dcim.device"

    def right_page(self):
        device = self.context["object"]

        status = get_device_status(device)

        return render_to_string(
            "meu_plugin/inc/device_status.html",
            {
                "status": self.define_status_string(status),
            },
        )

    def define_status_string(self, status):

        if status["status"] == "online":
            return "ONLINE 🟢" + " Latência: " + status["latency"]

        return "OFFLINE 🔴"


template_extensions = [DeviceStatusExtension]