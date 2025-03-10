from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST']) # So ein Decorator ist eine Zusatzinformation ('Annotation'), die hier bedeutet: Ein POST-Request soll diese Methode anstossen
def echo_view(request):
    return Response({'echo': request.data})

@api_view(['GET'])
def ping(request):
    return Response({'message': 'pong'})