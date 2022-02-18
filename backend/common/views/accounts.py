import json
from json import JSONDecodeError

import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.models.models import Publisher, Reader, User
from common.serializers.accounts import (
    PublisherSerializer,
    ResestPasswordRequestSerializer,
    ResetPasswordSerializer,
    ReaderSerializer
)

class ReaderView(mixins.CreateModelMixin,mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,viewsets.GenericViewSet):
    
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request, *args,**kwargs):
        """
            Function that creates a new User
        """
        # TODO : send an email for activation
        
        data = ''
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            data = request.data
        
        if data and data != "":
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data["password"] = data["password"]
            serializer.save()
            # queryset = Reader.objects.all()
            # username = serializer.validated_data["username"]
            return Response(
                {"Success":True,
                 "message":"registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response({
                "success":False,
                "message":"There is no DATA"
            },
                            status=status.HTTP_406_NOT_ACCEPTABLE)
            
    def retrieve(self,request,username,*args,**kwargs):
        queryset = Reader.objects.all()
        reader = get_object_or_404(queryset, username=username)
        serializer = self.serializer_class(reader)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # TODO : add functions for changing email and password

class PublisherView(viewsets.GenericViewSet):
    
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny, )
    
    def create(self, request, *args,**kwargs):
        data = ''
        try:
            data = json.loads(request.body)
        except JSONDecodeError and UnicodeDecodeError:
            data = request.data

        if data and data != "":
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data["password"] = data["password"]
            serializer.save()
            
            # TODO : add email activation
            
            return Response(
                {
                    "Success":True,
                    "message":"registred successfully"
                },
                status=status.HTTP_201_CREATED,
            )
            
        else:
            return Response(
                {
                    "Success": False,
                    "message":"There is no DATA"
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

    def retrieve(self, request, username, *args,**kwargs):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, username=username)
        serializer = self.serializer_class(publisher)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #TODO : add destory, update and email activation
    

# TODO : add password reset classes
