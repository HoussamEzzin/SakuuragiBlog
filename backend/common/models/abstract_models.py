from operator import mod
from django import models

class Years(models.Model):
    year = models.CharField( max_length=25)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.year

class Module(models.Model):
    module = models.CharField(max_length=50)
    
    class Meta:
        abstract =True
    
    def __str__(self):
        return self.module

class Tag(models.Model):
    tag = models.CharField( max_length=40)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.tag
    
    