from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def ScannerPage(request):
    temp = loader.get_template('scanner.html')
    return HttpResponse(temp.render())