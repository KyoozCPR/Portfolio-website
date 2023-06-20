import django.shortcuts as shortcut
from django.http import HttpResponse, HttpRequest,  Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader

import django.contrib.sessions

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import SignUpForm, BaseForm





# Create your views here.
def index(request):
    index_template = loader.get_template('PollsApp/home/index.html')
    
    return HttpResponse(index_template.render())

def about(request):
    
    return shortcut.render(request, 'PollsApp/about/about.html')


def survey(request):
    return shortcut.render(request, "PollsApp/survey/survey.html")


def signup(request: HttpRequest):

    """

        CHECK IF THE FORM WAS SENT WITH THE POST METHOD AND 
        CREATE A NEW ISTANCE OF THE SignUpForm() object PASSING THE DATA FROM THE REQUEST 
        AND SAVE IT INTO THE DATABASE 

    """


    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            
            if not(form.cleaned_data.items() in User.objects.values()):
                
                new_user = User.objects.create_user(
                    form.cleaned_data.get("username"),
                    form.cleaned_data.get("user_email"),
                    form.cleaned_data.get("password"),
                    )


                return shortcut.redirect('index')

    else:
        form = SignUpForm()

    
    authenticated_notification = request.session.get("Notification_error")
  
    return shortcut.render(request, "PollsApp/signup/signup.html", {"form": form, "not_authenticaded_message": authenticated_notification})



def login(request):
    
    if request.method == "POST":
        form = BaseForm(request.POST)
        
        if form.is_valid():
            
            if not(form.cleaned_data.items() in User.objects.values()):
                
                new_user = User.objects.get(
                    form.cleaned_data.get("username"),
                    form.cleaned_data.get("user_email"),
                    form.cleaned_data.get("password"),
                    )
                

                return shortcut.redirect('index')

    else:
        form = BaseForm()

    
  
  
    return shortcut.render(request, "PollsApp/Login/login.html", {"form": form})


def greeting(request):
    pass


def search_user(request: HttpRequest, pk):
    if request.user.is_authenticated:
        try:
            searched_user = User.objects.get(username_iexact=pk)  

        except ObjectDoesNotExist:
            raise Http404("No MyModel matches the given query.")
    else:
        request.session["Notification_error"] = "You are not authenticated"
        return shortcut.redirect("signup")