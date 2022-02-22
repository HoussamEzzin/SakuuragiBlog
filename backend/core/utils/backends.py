from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate
    using either thier username or email address
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        user_model = get_user_model()
        
        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)
            
        try:
            user = user_model.objects.get(Q(**{user_model.USERNAME_FIELD: username}))
            if check_password(password, user.password):
                return user
        except user_model.DoesNotExist:
            pass
        
        
        try:
            user = user_model.objects.get(Q(email_iexact = username))
            
            if check_password(password, user.password):
                return user
        except user_model.DoesNotExist:
            user_model().set_password(password)
        
        