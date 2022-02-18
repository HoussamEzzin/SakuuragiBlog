from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken


"""
    not implemented yet.
"""

class SendEmail:
    
    def send_email(self,subject,user,body,to,absurl, cc=None):
        message = EmailMessage(
            subject = subject,
            body='Hello '
            + str(user.__getattribute__("username"))
            + ',\n'
            + str(body)
            +': \n'
            +absurl
            +"\n SakuuragiBlog,",
            to=[to],
            cc=cc,
        )
        message.send()
        print("sent!")
    
    def simple_email(self, subject, body, username, to):
        message = EmailMessage(
            subject=subject,
            body='Bonjour '
            +str(username)
            +',\n'
            +str(body)
            +': \n'
            +"\n SakuuragiBlog",
            to=[to],
        )
        message.send()
        

class SendActivation(SendEmail):
    
    def account_activation(self, request,account_type,user
                           ,subject,to):
        token = RefreshToken.for_user(user=user).access_token
        current_site = settings.FRONTEND_URL + settings.ACTIVATION_URL
        absurl = 'http://' + current_site + account_type +"/" +str(token)
        body = "Activate your account by clicking on this link"
        cc = [""]
        self.send_email(subject, user,body,to,absurl,cc)
    
    def password_reset(self, request, user, to):
        
        token = RefreshToken.for_user(user=user).access_token
        current_state = settings.FRONTEND_URL
        relativeLink = settings.PASSWORD_RESET_URL
        absurl = 'http://' + current_state + relativeLink + str(token)
        body = "To reset your password, click on this link"
        self.send_email("password reset",user,body,to,absurl)