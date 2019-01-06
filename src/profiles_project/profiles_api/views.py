from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

# Create your views here.

class HelloWorldApi(APIView, Response):
    '''A Simple Hello Wolrd API '''

    serializer_class = serializers.HelloSerializers

    def get(self , request , format=None):

        an_api = [
            'Hello world api',
            'to get a response from view'
        ]

        return Response({'message':'Hello','an_api': an_api})

    def post(self , request):
        '''Create a hello message with name'''

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors)

    def delete(self,request,pk=None):
        '''create a delete method'''
        return Response({'method':'Delete'})

    def patch(self,request,pk=None):
        return Response({'method':'Pacth'})
