from django.urls import path, include
from . import views

urlpatterns = [
    path('scan_data', views.get_scan_data, name='get_scan_data'),
    path('report', views.get_report, name='get_report'),
]


