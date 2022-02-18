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
        Updaye personal information's Publisher
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
            #uncomplete