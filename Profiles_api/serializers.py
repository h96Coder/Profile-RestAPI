from rest_framework import serializers

class UserSerilizer(serializers.Serializer):
    "Serialize the name of user"
    name=serializers.CharField(max_length=10)