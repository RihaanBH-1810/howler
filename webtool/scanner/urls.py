from django.urls import path, include
from . import views

urlpatterns = [
    path('url', views.get_url, name='get_url'),
    path('report', views.get_report, name='get_report'),
]
