from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
