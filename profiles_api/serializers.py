from rest_framework import serializers
from . import models


class TodolistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.List
        fields = "__all__"
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = ('name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        def create(self, validated_data):
            user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

            return user