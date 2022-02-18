from email.policy import HTTP
from functools import partial
import json
from json import JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, status, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.models import *
from common.serializers.modelsSerializers import *


class ArticleView(viewsets.GenericViewSet):
    
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    def get_permissions(self):
        if self.action == 'get_articles':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_articles(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(
            {
                "Success": True,
                "message": "data loaded successfully",
                "article_list": serializer.data,
            },
            status=status.HTTP_201_CREATED
        )

    def add_article(self,request):
        data = ''
        try:
            data = json.loads(request.body)
        except JSONDecodeError and UnicodeDecodeError:
            data = request.data
        
        if data and data!= "":
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            article = serializer
            queryset = Article.objects.filter(
                article_author_id = data['author']
            )
            serializer = self.serializer_class(queryset, many=True)
            return Response(
                {
                    "Success":True,
                    "message":"Article added successfully",
                    "data": serializer.data,
                    "article": article.data
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"Success": False, "message": "There is no DATA"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )
    
    def add_article_picture(self,request,id,*args,**kwargs):
        try:
            data = json.loads(request.body)
        except JSONDecodeError and UnicodeDecodeError:
            data = request.data

        if data and data != "":
            model = get_object_or_404(Article,pk=id)
            serializer = ArticleSerializer(model, data=data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                article = serializer
                queryset = Article.objects.filter(
                    author=serializer.data['']
                )
        
    def get_article_by_id(self,request, pk=None,*args,**kwagrs):
        queryset = self.get_queryset(pk=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "Success": True,
            "message":"done",
            "article": serializer.data,
        },
                        status=status.HTTP_201_CREATED)
    
    def get_article_by_category(self, request, *args,**kwargs):
        try:
            data = json.loads(request.body)
        except JSONDecodeError and UnicodeDecodeError:
            data = request.data
        
        queryset = Category.objects.filter(
            article_category={'category_name': data['search']}
        )
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(
            {
                "Success":True,
                "message":"data loaded successfully",
                "results": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
    
    
    
    def destroy_article(self,request, pk=None):
        try:
            Article.objects.get(pk=pk).delete()
        except ObjectDoesNotExist:
            return Response(
                {
                    "Success": False,
                    "Exception": "Data not found"
                },status = status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {
                "Success": True,
                "message": "Article deleted successfully",
                "id_article": pk,
            },
            status= status.HTTP_201_CREATED,
        )
        
    