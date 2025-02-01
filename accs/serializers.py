# from django.contrib.auth.models import User
from .models import MyUser
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model =MyUser 
        fields = ['id','email','password']

        extra_kwargs = {'password': {'write_only':True}}

    def create(self,validated_data):
        user = MyUser.objects.create_user(**validated_data)

        return user






