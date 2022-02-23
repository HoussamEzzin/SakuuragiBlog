
import json
from json import JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from common.models.models import  Publisher
from common.serializers.auth import UserSerializer



class PublisherView(viewsets.GenericViewSet, generics.ListAPIView):
    
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Publisher.objects.all().filter(is_active=True)
    
    def get_publishers(self, request, *args, **kwargs):
        data = None
        try:
            data = json.loads(request.data)
        except JSONDecodeError:
            data = request.data

        if data and data is not None:
            try:
                users = self.request.filter(**data).values()
                return Response(
                    {
                        "Success": True,
                        "message": "data loaded successfully",
                        "publishers_list": users,
                    },
                    status= status.HTTP_200_OK,
                )
            except ObjectDoesNotExist:
                return Response({
                    "Success": False,
                    "message": "User does not exist",
                },
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "Success":False,
                "message": "There is no Data",
            },
                            status=status.HTTP_406_NOT_ACCEPTABLE,)

class PublisherNoAthenticatedView(viewsets.GenericViewSet, generics.ListAPIView):
    
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset=(
        Publisher.objects.all()
        .filter(is_active=True)
        .order_by('-profle_pic','-description')
    )
    
    def get_publishers_no_authentication(self, request, *args, **kwargs):
        data = None
        try:
            data = json.loads(request.body)
        except JSONDecodeError:
            data = request.data
        
        if data and data is not None:
            try:
                users = self.queryset.filter(**data).values()
                return Response(
                    {
                        "Success":True,
                        "message": "data loaded successfully",
                        "publishers_list": users,
                    },
                    status = status.HTTP_200_OK,
                )
            except ObjectDoesNotExist:
                return Response(
                    {"Success":False,
                     "message":"User Doesn't exist!"},
                    status= status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"Success": False,
                 "message":"There is no Data"},
                status = status.HTTP_406_NOT_ACCEPTABLE,
            )