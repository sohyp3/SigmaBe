from django.shortcuts import render
# from django.contrib.auth.models import User
from .models import MyUser

from rest_framework import generics
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated,AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]


