from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class" : "widgets-field"})   

    
    class Media:
        abstract = True



class SignUpForm(forms.ModelForm, BaseForm):
    class Meta:
        model = User 
        fields = ["username", "email", "password"]
        widgets = {
            "username" : forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            "email"    : forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            "password" : forms.PasswordInput(attrs={'placeholder': "Enter a password"}) 
        }


    def save(self, *args, **kwargs):
        if self.is_valid():
            user = super().save(commit=False, *args, **kwargs)
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.set_password(self.cleaned_data.get("password"))
            user.save()
            return user




class LoginForm(BaseForm, forms.Form):
    email = forms.EmailField(max_length=130,
                               widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=128,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))  


     


    


 



    


    
    


    

        

  
    

    


