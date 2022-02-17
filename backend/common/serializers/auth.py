from asyncore import read
from dataclasses import fields
from rest_framework import serializers

from common.models.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}
        
        read_only_fields = (
            "id",
            "username",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
            "groups",
            "user_permissions",
            "is_reader",
            "is_publisher",
        )