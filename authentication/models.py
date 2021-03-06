from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
# custom model for user
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('firstname', None)
        extra_fields.setdefault('lastname', None)
        #extra_fields.setdefault('profilePicture', None)
        extra_fields.setdefault('email', None)
        extra_fields.setdefault('telephone', None)
        if username is None:
            raise TypeError('Users should hava a username')
        if email is None:
            raise TypeError('Users should have an Email')

        user = self.model(username = username, email = self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

# create superUser
    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    firstname       = models.CharField(max_length=50, null=True)
    lastname        = models.CharField(max_length=50, null=True)
    telephone       = models.CharField(max_length=11, null=True, unique=True)
    username        = models.CharField(max_length=255, unique= True, db_index=True) 
    # db_index to search by username
    email           = models.EmailField(max_length=255, unique=True, db_index=True)
    roles           = models.CharField(default="psg",max_length= 10)
    profilePicture  = models.FileField(max_length=None,blank=True,null=True, default=None)
    is_verified = models.BooleanField(default=True)
     # we set is because the email to verify was needed
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #TO TELL DJANGO TO USE USERNAIM 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        return ''
    
    