from django.db import models

from dcim.models import Device


class DeviceMonitor(models.Model):

    device = models.OneToOneField(
        Device,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20
    )

    latency = models.CharField(
        max_length=50
    )

    last_check = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Device Monitor"

    def __str__(self):
        return f"{self.device.name} - {self.status}"
