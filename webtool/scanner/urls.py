from django.urls import path, include
from . import views

urlpatterns = [
    path('main', views.ScannerPage, name='scanner'),
]
