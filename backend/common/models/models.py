import email
import uuid



from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils import timezone
from djongo import models


from common.models.abstract_models import Module, Tag, Years


class UserManager(BaseUserManager):
    
    # abstract method for creating users
    def _create_user(
        self, username, email, password, is_staff, is_superuser, **extra_fields
    ):
        if not email:
            raise ValueError("A valid username must be set")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        now = timezone.now()
        user = self.model(
            username= username,
            email=email,
            last_login= now,
            date_joined= now,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,
                         password, **extra_fields):
        return self._create_user(
            username, email, password, True, True, **extra_fields
        )
        
    def get_by_natural_key(self):
        return self.get(email=email)
    

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField( max_length=254, unique=True)
    is_reader = models.BooleanField('reader status', default=False)
    is_publisher = models.BooleanField('publisher status',default=False)
    is_featured = models.BooleanField('is Featured user', default=False)
    profile_pic = models.CharField(max_length=255, default="")
    description = models.TextField(default="",null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=True,blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True)
    
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    objects = UserManager()
    
    class Meta:
        app_label = "common"
        verbose_name_plural = "Admin Users"
    
    def get_email(self):
        email_field_name = self.get_email_field_name()
        return getattr(self, email_field_name,None)
    
    def set_email(self, new_mail):
        email_field_name = self.get_email_field_name()
        return setattr(self, email_field_name, new_mail)
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name


class ReaderManager(BaseUserManager):
    
    def _create_user(self, email,password,**extra_fields):
        if not email:
            raise ValueError("A valid username must be set")
        email = self.normalize_email(email)
        username = self.model.normalize_username(extra_fields["username"])
        extra_fields.pop("username")
        now = timezone.now()
        reader = self.model(
            username = username,
            email = email,
            last_login = now,
            date_joined = now,
            is_staff = False,
            is_active = False,
            **extra_fields
        )
        reader.set_password(password)
        reader.save()
        return reader
    
    def create_reader(self, email,password,**extra_fields):
        return self._create_user(email,password,**extra_fields)
    

class PublisherManager(BaseUserManager):
     def create_publisher(self, email,password, **extra_fields):
         if email is None:
             raise TypeError("Users must have an email address")
         now = timezone.now()
         publihser = Publisher(
             email=self.normalize_email(email),
             is_staff = False,
             is_active = False,
             is_superuser = False,
             last_login = now,
             date_joined = now,
             **extra_fields
         )
         publihser.set_passowrd(password)
         publihser.save()
         return publihser

class Reader(User):
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]
    
    objects = ReaderManager()
    
    class Meta:
        verbose_name_plural = "Readers"
    
    def __str__(self):
        return self.email + " - is_reader"

class Publisher(User):
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]
    
    objects = PublisherManager()
    
    class Meta:
        verbose_name_plural = "Publishers"
    
    def __str__(self):
        return self.email + " - is_publisher"

class Category(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    category_name = models.CharField(max_length=200, default="default")
    
    objects = models.DjongoManager()
    
    def __str__(self):
        return self.category_name



class Article(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,
                          editable=False)
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    article_pic = models.ImageField(
        null = True,
        upload_to='images',
    )
    author = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # on_delete= models.CASCADE if the user get deleted, the post is deleted aswell
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    content = models.TextField()
    
    objects = models.DjongoManager()
    
    def __str__(self):
        return self.title 

class ArticleComment(models.Model):
    
    user = models.ForeignKey(Reader, on_delete=models.CASCADE, default=None)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)
    comment = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.comment

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                          editable=False)
    notif_date = models.DateTimeField(default=timezone.now)
    message = models.CharField(max_length=200)
    read = models.BooleanField('read status', default=False)
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None,
        related_name='receiver'
    )
    
    link = models.CharField(max_length=400, default=None)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, related_name='sender'
    )
    
    def __str__(self):
        return self.message
         
