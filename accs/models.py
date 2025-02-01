from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyUserManger(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        return self.create_user(email,password,**extra_fields)
    


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

    objects=MyUserManger()
    def __str__(self):
        return self.email       
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
# Create your models here.
