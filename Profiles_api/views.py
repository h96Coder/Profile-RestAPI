from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
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