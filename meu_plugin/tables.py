import django_tables2 as tables

from django.utils.safestring import mark_safe

from dcim.models import Device

from .utils import get_device_status


class DeviceMonitorTable(tables.Table):

    name = tables.LinkColumn(
        viewname="dcim:device",
        args=[tables.A("pk")]
    )

    monitor_status = tables.Column(
        empty_values=(),
        verbose_name="Monitor"
    )

    latency = tables.Column(
        empty_values=(),
        verbose_name="Latency"
    )

    last_check = tables.Column(
        empty_values=(),
        verbose_name="Last Check"
    )

    class Meta:

        model = Device

        template_name = "django_tables2/bootstrap.html"

        fields = (
            "name",
            "primary_ip4",
            "status",
            "monitor_status",
            "latency",
            "last_check"
        )

    def render_monitor_status(self, record):

        result = get_device_status(record)

        status = result["status"]

        if status == "online":
            return mark_safe(
                '<span class="badge bg-success">ONLINE</span>'
            )

        elif status == "offline":
            return mark_safe(
                '<span class="badge bg-danger">OFFLINE</span>'
            )

        return mark_safe(
            '<span class="badge bg-secondary">UNKNOWN</span>'
        )

    def render_latency(self, record):

        result = get_device_status(record)

        latency = result["latency"]

        if latency == "timeout":
            return mark_safe(
                '<span class="badge bg-danger">timeout</span>'
            )

        try:

            value = float(latency.replace(" ms", ""))

            if value < 20:

                color = "success"

            elif value < 80:

                color = "warning"

            else:

                color = "danger"

            return mark_safe(
                f'<span class="badge bg-{color}">{latency}</span>'
            )

        

        except Exception:

            return latency

    def render_last_check(self, record):

        from .models import DeviceMonitor

        monitor = DeviceMonitor.objects.filter(
            device=record
        ).first()

        if not monitor:
            return "-"

        from django.utils.timezone import localtime

        local_time = localtime(monitor.last_check)

        return local_time.strftime(
            "%d/%m/%Y %H:%M:%S"
        )