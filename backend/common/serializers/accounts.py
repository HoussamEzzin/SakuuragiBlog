from dataclasses import fields
from rest_framework import serializers
from common.models.models import Reader, Publisher

class ReaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reader
        fields = "__all__"
        extra_kwargs = {'password' : {'write_only':True}}
        read_only_fields = (
            "id",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        )
        
    def create(self,validated_data):
        email = validated_data.get("email",None)
        password = validated_data.get("password",None)
        validated_data.pop("email")
        validated_data.pop("password")
        
        return Reader.objects.create_reader(email,password,**validated_data)
    
class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = "__all__"
        extra_kwargs = {'password':{'write_only':True}}
        read_only_fields = (
            "id",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        )
        
    def create(self, validated_data):
        email = validated_data.get("email",None)
        password = validated_data.get("password",None)
        validated_data.pop("email")
        validated_data.pop("password")
        
        return Publisher.objects.create_publisher(email,password,**validated_data)
    
    
class ResestPasswordRequestSerializer(serializers.Serializer):
    
    email = serializers.EmailField(min_length=2)
    
    class Meta:
        fields = ['email']

class ResetPasswordSerializer(serializers.Serializer):
    
    password = serializers.CharField(min_length=2)
    
    class Meta:
        fields = ['password']