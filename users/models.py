from django.db import models
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_Superuser(self,email,password,name,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_staff') is not True:
            return ValueError('superuser must be staff')

        if other_fields.get('is_superuser') is not True:
            return ValueError('superuser must be superuser')    

        return self.createuser(email,password,name,**other_fields)

    def createuser(self,email,password,name,**other_fields):
       if not email:
           raise ValueError('You should Provide A Valid Email.')
       email = self.normalize_email(email) 
       user = self.model(email=email,name=name,**other_fields) 

       user.set_password(password) 