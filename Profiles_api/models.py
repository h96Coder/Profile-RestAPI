from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class UserProfileManger(BaseUserManager):

    def create_user(self,email,name,password):
        if not email:
           raise  ValueError("Email not entered")
        email =self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user= self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)



class UserProfile(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(max_length=200,unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.email

# Create your models here.
