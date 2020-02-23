from rest_framework import serializers
from . import models
class UserSerilizer(serializers.Serializer):
    "Serialize the name of user"
    name=serializers.CharField(max_length=10)
class UserProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields =('name','email','id','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        """Create new user and return it"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile','created_on','status_text')
        extra_kwargs={'user_profile':{'read_only':True}}

