import django.shortcuts as shortcut
from django.http import HttpResponse, HttpRequest,  Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
import django.contrib.sessions
from django.contrib.auth import authenticate, login
from .models import User 
from .forms import SignUpForm, BaseForm, LoginForm





# Create your views here.
def index(request: HttpRequest):
    return shortcut.render(request, 'PollsApp/home/index.html')


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

    if request.user.is_authenticated == True:
        request.session["Authenticated_Message": "You are already authenticated"]
        shortcut.redirect("index")


    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()

            authenticated_user = authenticate(
                username = form.cleaned_data.get("username"), 
                password = form.cleaned_data.get("password")
                )

            if authenticated_user is not None:
                login(request, authenticated_user)
                return shortcut.redirect('index')

    else:
        form = SignUpForm()

    
  
    return shortcut.render(
        request, 
        "PollsApp/signup/signup.html",

        {"form": form})



def login_func(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():


            authenticated_user = authenticate(
            username = form.cleaned_data.get("username"), 
            password = form.cleaned_data.get("password")
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return shortcut.redirect('index')
            else: 
                request.session["Notification_error"] = "You are not authenticated"

    else:
        form = LoginForm()

    return shortcut.render(
        request, 
        "PollsApp/Login/login.html",

        { 
            "form": form,

    
        }
        )

def logout(request: HttpRequest):

    signup_message = request.session.get("Authenticated_Message")

    if signup_message != None:
        return shortcut.render(request, 'PollsApp/home/index.html', {"allert" : signup_message})
    
  
  
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
    
