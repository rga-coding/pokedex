from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginSerializer(AuthTokenSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

