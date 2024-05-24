from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError



def clean_email(value):
    if User.objects.filter(email__iexact=value).exists():
        ValidationError("Your email address is already in use!")
    return value
        



"""

 Custom user manager used as an interface through a Queryset to make querys and create new users

 
"""
class UserManagerCustom(BaseUserManager):

    def create_user(self, username: models.CharField, email: models.EmailField, password: models.CharField=None):
        if not(username) or not(email):
            raise ValueError("Can't create User without required fields!")

        
        user = self.model(username, email)
        self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, username, email, password=None):
        if not(username) or not(email):
            raise ValueError("Can't create User without required fields!")

        
        user = self.model(username, email)
        self.normalize_email(email)
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user
    
"""

 Custom User model with username field set as a identifier for the authentication backend 

"""

class User(AbstractBaseUser):

    username = models.CharField(max_length=30, blank=False, unique=True)
    email    = models.EmailField(max_length=150, blank=False, unique=True, validators=[clean_email], default="string")
    is_admin = models.BooleanField(default=False)
    objects  = UserManagerCustom()


    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

   
    
        


    


    
    




