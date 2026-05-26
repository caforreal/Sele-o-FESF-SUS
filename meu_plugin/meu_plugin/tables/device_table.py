import django_tables2 as tables

from dcim.tables.devices import DeviceTable
from meu_plugin.utils import get_device_status


class DeviceStatusColumn(tables.Column):

    def render(self, value, record):
        status = get_device_status(record)

        if status == "online":
            color = "green"
        elif status == "offline":
            color = "red"
        else:
            color = "gray"

        return f'''
        <span style="
            padding:4px 8px;
            border-radius:6px;
            background:{color};
            color:white;
            font-weight:bold;
        ">
            {status.upper()}
        </span>
        '''


class MeuDeviceTable(DeviceTable):

    status_monitor = DeviceStatusColumn(
        empty_values=(),
        verbose_name="Monitor"
    )

    class Meta(DeviceTable.Meta):
        fields = DeviceTable.Meta.fields + ("status_monitor",)
