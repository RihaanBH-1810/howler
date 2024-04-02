from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from scripts.Controller.controller import controller, generate_report
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
import json 

@api_view(['POST'])
def get_url(request):
    
    config = request.data['config']
    # config = json_res["config"]
    # url = json_res["url"]
    url = request.data['url']
    # config = request.GET.dict(['config'])
    if config != {}:
        #controller(url, config)
        return Response({'url': url, 'config': config})
    else:
        #controller(url)
        return Response({'url': url})


@api_view(['GET'])
def get_report(request):
    done = generate_report()
    if done:
        report = loader.get_template('report.html')
        return Response(report)
    else:
        return Response("Error generating report !")
