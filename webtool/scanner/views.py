from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from scripts.controller import controller, generate_report
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_scan_data(request):
    config = request.data['config']
    url = request.data['url']
    if config != {}:
        controller(url, config)
        return Response({'url': url, 'config': config})
    else:
        controller(url)
        return Response({'url': url})

@api_view(['GET'])
def get_report(request):
    done = True
    if done:
        report = render(request, 'report.html', {})
        return HttpResponse(report)
    else:
        return Response("Error generating report !")