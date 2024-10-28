from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError



def clean_email(value):
    if User.objects.filter(email__iexact=value).exists():
       raise ValidationError("Your email address is already in use!", code="invalid")
   
    
class UserManagerCustom(BaseUserManager):

    def create_user(self, username: models.CharField, email: models.EmailField, password: models.CharField=None):
        if not(username) or not(email):
            raise ValueError("Can't create User without required fields!")

        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
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
    email    = models.EmailField(max_length=150, blank=False, unique=True, validators=[clean_email])
    is_admin = models.BooleanField(default=False)
    objects  = UserManagerCustom()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']



"""
When we want to store additional information about a user 
which is not related to authentication, 
we can create a new model which has a one-to-one link with the user.
creating a User Profile model with:
    - one relationship with the user model
    - a bio
    - an image

"""

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #the models.CASCADE means that if a user is deleted, it deletes also his profile as well
    bio = models.TextField()
    image = models.ImageField(upload_to="media")

    def __str__(self):

       return self.user.username
       
   
   
    


        

    
    




    
    




