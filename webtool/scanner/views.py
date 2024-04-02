from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from scripts.Controller.controller import controller
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   

@api_view(['POST'])
def get_url(request):
    url = request.data['url']
    controller(url)
    return Response({'url': url})



