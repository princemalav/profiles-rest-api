from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloWorldApi(APIView, Response):
    '''A Simple Hello Wolrd API '''

    def get(self , request , format=None):

        an_api = [
            'Hello world api',
            'to get a response from view'
        ]

        return Response({'message':'Hello','an_api': an_api})
