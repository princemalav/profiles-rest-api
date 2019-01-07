from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from . import serializers , models

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


class HelloViewset(viewsets.ViewSet):
    '''Test our viewset'''

    serializer_class  = serializers.HelloSerializers

    def list(self,request):
        '''viewset'''
        a_viewset=[
            'use of list , create,update function']

        return Response({'message':'Hello','list_view':a_viewset})

    def create(self,request,pk=None):
        '''Create a new hello message'''

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)

            return Response({'message':message})

        else:
            return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'method':'Partial Put'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    '''handles creating updating profile'''

    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
