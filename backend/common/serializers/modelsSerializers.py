# Category, ArticlePart, Article, ArticleComment, Notification

from dataclasses import fields
from rest_framework import serializers

from common.models.models import (
    Category, Article, ArticleComment, Notification,
    User
)


        

class ArticleSerializer(serializers.ModelSerializer):
    
 
    
    class Meta:
        model = Article
        fields = "__all__"
        
class ArticleCommentSerializer(serializers.ModelSerializer):
    
    user_pic = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = ArticleComment
        fields = "__all__"
        
    def get_user_pic(self,obj):
        queryset = User.objects.get(id = obj.user.id)
        return queryset.profile_pic
    
    def get_username(self, obj):
        queryset = User.objects.get(id=obj.user.id)
        return queryset.username

class NotificationSerializer(serializers.ModelSerializer):
    
    notification = serializers.SerializerMethodField()
    
    class Meta:
        model = Notification
        fields = "__all__"
    
    def get_notification_pic(self,obj):
        queryset = User.objects.get(id=obj.sender.id)
        return queryset.profile_pic

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        