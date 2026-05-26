from netbox.plugins import PluginConfig
from .template_extensions import template_extensions 
from .navigation import menu_items   


class MeuPluginConfig(PluginConfig):
    name = "meu_plugin"
    verbose_name = "Network Status Monitor"
    description = "Plugin simples"
    version = "0.1"
    author = "@caforreal"

    base_url = "meu-plugin"

    template_extensions = "template_extensions"
    menu_items = "menu_items"

config = MeuPluginConfig