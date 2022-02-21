from functools import partial
import json
from json import JSONDecodeError

from django.contrib.auth import authenticate, login
from rest_framework import authentication, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from common.models.models import Publisher, User
from common.serializers.accounts import ReaderSerializer,PublisherSerializer
from common.serializers.auth import UserSerializer
from common.views.accounts import PublisherView

class UserUpdateView(viewsets.GenericViewSet, UpdateModelMixin):
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    
    def user_update(self, request, *args, **kwargs):
        data = ''
        try:
            data = json.loads(request.body)
        except:
            data = request.data
        
        if data and data != "":
            instance = self.get_object()
            serializer = self.serializer_class(
                instance, data=data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            token, _ = Token.objects.get_or_create(user=instance)
            return Response(
                {
                    "Success": True,
                    "token": token.key,
                    "message": "your data are updated successfully",
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "Success": False,
                    "message":"There is an error in the server",
                },
                status = status.HTTP_406_NOT_ACCEPTABLE,
            )

class PublisherUpdateView(viewsets.GenericViewSet, UpdateModelMixin):
    
    """
        Update personal information's Publisher
    """
    
    authentication_classes = [TokenAuthentication]
    serializer_class = PublisherView
    permission_classes = (AllowAny,)
    queryset = Publisher.objects.all()
    
    def publisher_update(self, request, pk=None, *args,**kwargs):
        data = ''
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            data = request.data
        
        if data and data != "":
            instance = self.get_object()
            serializer = self.serializer_class(
                instance, data=data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            token, _ = Token.objects.get_or_create(user=instance)
            return Response({
                "Success":True,
                "token":token.key,
                "message":"Your data are updated successfully",
                "user": serializer.data,
            },
                            status=status.HTTP_201_CREATED,)
        else:
            return Response({
                "Success":False,
                "message":"There is an error"
            },
                            status=status.HTTP_406_NOT_ACCEPTABLE,)
            

class UserLognView(viewsets.GenericViewSet):
    
    serializer = UserSerializer
    permission_classes = (AllowAny,)
    
    def login(self,request, *args,**kwargs):
        data = ""
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            data = request.data
        
        email = data.get("email",None)
        password = data.get("password",None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                if user.is_reader:
                    returned_data = ReaderSerializer(user).data
                elif user.is_publisher:
                    returned_data = PublisherSerializer(user).data
                else:
                    return Response(
                        {
                            "Success": False,
                            "message": "User doesn't have a type",
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )
                login(request,user)
                token, _ = Token.objects.get_or_create(user=user)
                serializer = self.serializer_class(user)
                return Response({
                    "Success":True,
                    "token": token.key,
                    "user": dict(returned_data, **serializer.data),
                },
                                status=status.HTTP_200_OK,)
            else:
                return Response({
                    "Success":False,
                    "message":"User is not Active"
                },status=status.HTTP_404_NOT_FOUND,)
        else:
            return Response(
                {
                    "Success":False,
                    "message": "wrong username or password!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

class LogoutView(viewsets.GenericViewSet):
    
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def logout(self,request,*args,**kwargs):
        try:
            data = json.loads(request.body)
            Token.objects.filter(user_id=data["user_id"]).delete()
        except KeyError:
            return Response(
                {
                    "Success": False,
                    "message": "Bad request"
                },
                status = status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "Success": True,
                "message": "Logged out successfully"
            },
            status=status.HTTP_200_OK,
        )