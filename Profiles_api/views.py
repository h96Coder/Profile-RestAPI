from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
class HelloApiView(APIView):
    """Test API"""
    serializer=serializers.UserSerilizer
    def get(self,request,format=None):
        """Return API response"""
        an_apiview=[
            'Uses HTTP methods as funtion get,post,put,delete,patch',
            'is it similar to traditional Djangpo api',
            'Gives the flexible Django API',
            'it mapped manually'
        ]
        return Response({'message':'Django First API','an_apiview':an_apiview})
    def post(self,request,format=None):
        serializer=self.serializer(data=request.data)
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            return Response(f'Hello {name}')
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'Method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    serializer = serializers.UserSerilizer
    def list(self,request,pk=None):
        lst=['Hello ViewSet ',
             'Uses Action (list, create,retrieve,update,partial_update',
             'Automatically maps to Urls using Routers',
             'Provides more funtionality with code',]
        return Response({'message':'Hello','a_viewset':lst})

    def create(self, request, format=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response(f'Hello {name}')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({'method':'GET'})
    def update(self,request,pk=None):
        return Response({'method':'PUT'})
    def partial_update(self,request,pk=None):
        return Response({'method':'PATCH'})
    def destroy(self,request,pk=None):
        return Response({'method':'DELETE'})