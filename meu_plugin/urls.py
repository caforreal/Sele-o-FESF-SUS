from django.urls import path

from .views import monitor_view

urlpatterns = [

    path(
        "monitor/", 
        monitor_view,
        name="monitor"
    ),

]