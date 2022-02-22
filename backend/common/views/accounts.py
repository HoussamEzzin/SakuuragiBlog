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

from core.utils.email import SendActivation


class ReaderView(SendActivation,mixins.CreateModelMixin,mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,viewsets.GenericViewSet):
    
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request, *args,**kwargs):
        """
            Function that creates a new User with email activation
        """
        
        
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
            queryset = Reader.objects.all()
            username = serializer.validated_data["username"]
            self.account_activation(
                request,
                "reader",
                get_object_or_404(queryset,username=username),
                "Activation",
                to=data["email"],
            )
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
    
    # TODO : add update user info function
    
    def activated(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            reader = Reader.objects.get(id=payload['user_id'])
            if not reader.is_active:
                reader.is_active = True
                reader.save()
            return Response({
                'message':'Activation Expired'
            },
                            status=status.HTTP_200_OK)
        except jwt.exceptions.ExpiredSignatureError:
            return Response(
                {'error':'Activation Expired'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError:
            return Response(
                {'error': 'Invalid token'},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def set_password(self, request, username, *args, **kwargs):
        queryset = Reader.objects.all()
        reader = get_object_or_404(queryset, username=username)
        data = request.data
        serializer = self.serializer_class(reader, data=data)
        serializer.is_valid(raise_exception=True)
        reader.set_password(make_password(serializer.validated_data['password']))
        reader.is_active = False
        reader.save()
        self.account_activation(
            request, "reader", reader, "Password changed", to=reader.get_email()
        )
        return Response(serializer.data)

    def set_email(self, request,username, *args, **kwargs):
        queryset = Reader.objects.all()
        reader = get_object_or_404(queryset, username=username)
        data = request.data
        serializer = self.serializer_class(reader, data=data)
        serializer.is_valid(raise_exception=True)
        reader.set_email(serializer.validated_data['email'])
        reader.is_active = False
        reader.save()
        self.account_activation(
            request, "reader", reader, "email changed",to=reader.get_email()
        )
        return Response(serializer.data)
    
    

class PublisherView(SendActivation,viewsets.GenericViewSet):
    
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
            
            queryset = Publisher.objects.all()
            username = serializer.validated_data["username"]
            self.account_activation(
                request,
                "publisher",
                get_object_or_404(queryset, username=username),
                "Activation",
                to=data["email"],
            )
            
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
    
    #TODO : add destory, update 
    
    def activated(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            publisher = Publisher.objects.get(id=payload['user_id'])
            if not publisher.is_active:
                publisher.is_active = True
                publisher.save()
            return Response(
                {'message': 'Successfully activated',
                 "Success": True},
                status= status.HTTP_200_OK,
            )
        except jwt.exceptions.ExpiredSignatureError:
            return Response(
                {'error':'Activation expired'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError:
            return Response(
                {'error': 'Invalid token'},
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def set_password(self,request, username, *args, **kwargs):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, username=username)
        data = request.data
        serializer = self.serializer_class(publisher, data=data)
        serializer.is_valid(raise_exception=True)
        publisher.set_password(make_password(serializer.validated_data['password']))
        publisher.is_active = False
        publisher.save()
        self.account_activation(
            request,
            "publisher-activated",
            publisher,
            "password changed",
            to=publisher.get_email(),
        )
        return Response(serializer.data)
    def set_email(self,request, username, *args, **kwargs):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, username=username)
        data = request.data
        serializer = self.serializer_class(publisher, data=data)
        serializer.is_valid(raise_exception=True)
        publisher.set_email(serializer.validated_data['email'])
        publisher.is_active = False
        publisher.save()
        self.account_activation(
            request,
            "publisher-activated",
            publisher,
            "email changed",
            to=publisher.get_email()
        )        
        return Response(serializer.data)
    
class RequestPasswordReset(viewsets.GenericViewSet, SendActivation):
    
    serializer_class = ResestPasswordRequestSerializer
    permission_classes = (AllowAny,)
    
    def request_password_reset(self, request, *args, **kwargs):
        
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            data = request.data

        email = data['email']
        
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email=email)
            self.password_reset(request, user, to=email)
        return Response(
            {
                'Success': True,
                'message': 'We have sent you a link to reset your password,'
            },
            status=status.HTTP_200_OK,
        )

class PasswordReset(viewsets.GenericViewSet):
    
    serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)
    
    def password_reset(self, request):
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            data = request.data 
        
        token = data.get('token',None)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if user.is_active:
                serializer = self.serializer_class(user, data=data)
                serializer.is_valid(raise_exception=True)
                user.set_password(data['password'])
                user.save()
                return Response({
                    'Success':True,'password':'Successfully changed'
                },
                                status=status.HTTP_200_OK)
        except jwt.exceptions.ExpiredSignatureError:
            return Response({
                'error': 'lien expired'
            },status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({
                'error':'invalid token'
            },
                            status=status.HTTP_400_BAD_REQUEST)