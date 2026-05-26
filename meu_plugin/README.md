# NetBox Network Monitor Plugin

A custom NetBox plugin for real-time device monitoring using ICMP ping.

---

# Features

* Real-time device monitoring
* ICMP ping status checking
* Online / Offline / Unknown status
* Latency monitoring
* Automatic refresh
* Search bar for devices
* Dashboard cards
* Color-coded latency badges
* Integration with NetBox sidebar menu
* Direct navigation to device pages
* Persistent monitoring data

---

# Dashboard Preview

The plugin provides a monitoring dashboard directly inside NetBox.

Features available in the dashboard:

* Online device count
* Offline device count
* Unknown device count
* Average latency
* Device search
* Device monitoring table
* Clickable device links

---

# Technologies Used

* Python
* Django
* NetBox Plugin Framework
* django-tables2
* ICMP Ping

---

# Project Structure

```text
meu_plugin/
├── migrations/
├── templates/
│   └── meu_plugin/
│       ├── home.html
│       └── inc/
├── __init__.py
├── models.py
├── plugin.py
├── navigation.py
├── tables.py
├── template_extensions.py
├── urls.py
├── utils.py
└── views.py
```

---

# Installation

## Clone repository

```bash
git clone https://github.com/caforreal/netbox-device-monitor-plugin.git
```

---

## Install plugin

Inside your NetBox environment:

```bash
pip install -e .
```

---

## Enable plugin in NetBox

Edit:

```python
netbox/netbox/configuration.py
```

Add:

```python
PLUGINS = ["meu_plugin"]
```

---

## Run migrations

```bash
python netbox/manage.py makemigrations meu_plugin
python netbox/manage.py migrate
```

---

## Start server

```bash
python netbox/manage.py runserver
```

---

# How It Works

The plugin:

1. Reads devices from NetBox
2. Retrieves the Primary IPv4 address
3. Executes ICMP ping
4. Stores monitoring information in the database
5. Displays results in a dashboard

---

# Device Requirements

Each device should have:

* At least one interface
* An IP address assigned to the interface
* Primary IPv4 configured

Example:

```text
Device
 └── Interface (eth0)
      └── IP Address (8.8.8.8/32)
```

---

# Monitoring Status

| Status  | Meaning                  |
| ------- | ------------------------ |
| ONLINE  | Device responded to ping |
| OFFLINE | Device did not respond   |
| UNKNOWN | Missing interface or IP  |

---

# Latency Colors

| Color  | Latency  |
| ------ | -------- |
| Green  | < 20 ms  |
| Yellow | 20–80 ms |
| Red    | > 80 ms  |

---


# Author

Caroline Andrade

---

# License

MIT License
