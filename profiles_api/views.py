from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers

class HelloApiView(APIView):
    # Test api views
    serializer_class = serializers.HelloSerializer
    def get(self, request,format=None):
        # return a list of APIview features
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, push, delete)',
            'Is similar to a traditional django view',
            'Give you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        # create a hello message with our name
        serialzier = self.serializer_class(data=request.data)

        if serialzier.is_valid():
            name = serialzier.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serialzier.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        # handle updating an object
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        # handle a partial update of an object
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        # Delete a object
        return Response({'method':'Delete'})


class HelloViewSet(viewsets.ViewSet):
    # test api viewset
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        # return a hello message
        a_viewset = [
            'users actions (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs using Routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        # create a new hello message
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid:
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        # handle getting a object by its ID
        return Response({'http_method':'GET'})

    def update(self,request, pk=None):
        # handle updating an object
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        # handle updating part of an object
        return Reponse({'http_method':'PATCH'})
    def destroy(self,request,pk=None):
        # handle removing on object
        return Reponse({'http_method':'DELETE'})
