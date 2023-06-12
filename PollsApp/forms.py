from django import forms


"""
    Base class used to update each field of the form that is going to 
    inherit this base class with a specific HTML class 
     
"""

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields_name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'widgets-field'})
    
    username = forms.CharField(

        label="username", 
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
        )

    password = forms.CharField(

      label="Password", 
      max_length=100,
      widget=forms.PasswordInput(attrs={'placeholder':'Enter a password'})
      )


"""
    class used to rapresent a form, where each attribute is a different (the input logic for the user)
    and each field is assigned to a specif html input type through a widget
    and we can access the data passed by the user using the method cleaned_data()
    so that we can create o check a user in a data 
"""


class SignUpForm(BaseForm):

    user_email = forms.EmailField(

        label="Email", 
        max_length=150,
        widget=forms.EmailInput(attrs={'placeholder':'Enter your email'})
        )
    
  
    

    


