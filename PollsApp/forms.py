from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
"""
    Base class used to update each field of the form that is going to 
    inherit this base class with a specific HTML class 
     
"""

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class" : "widgets-field"})   

    
    class Media:
        abstract = True

    #when the is_valid() function is called, it is going to call the first three main methods for the field validation then the custom ones

"""                     
    class used to rapresent a form, where each attribute is a different field (the input logic for the user)
    and each field is assigned to a specific html input type through a widget
    and we can access the data passed by the user using the method cleaned_data()
    so that we can create o check a user in a data 
"""

class SignUpForm(forms.ModelForm, BaseForm):
    class Meta:
        model = User 
        fields = ["username", "email", "password"]
        widgets = {
            "username" : forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            "email"    : forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            "password" : forms.PasswordInput(attrs={'placeholder': "Enter a password"}) 
        }


    
    """
        when dealing with form validation we can overwrite or customize this processes that raise the ValidationError 
        exception when calling the is_valid() function on a form is called
        In the Django documentation as listed here: https://docs.djangoproject.com/en/4.2/ref/forms/validation/
        says that we can create custom form methods in the 'clean_<fieldname>()" format
    """
    
    #when the is_valid() function is called, it is going to call the first three main methods for the field validation then the custom ones
    




    def save(self, *args, **kwargs):
        if self.is_valid():
            user = super().save(commit=False, *args, **kwargs)
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.set_password(self.cleaned_data.get("password"))
            user.save()
            return user




class LoginForm(BaseForm, forms.Form):
    username = forms.CharField(max_length=130,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(max_length=128,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))  


     


    


 



    


    
    


    

        

  
    

    


