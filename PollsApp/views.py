import django.shortcuts as shortcut
from django.http import HttpRequest,  Http404
from django.core.exceptions import ObjectDoesNotExist
import django.contrib.sessions
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

user = get_user_model()



# Create your views here.
def index(request: HttpRequest):
    return shortcut.render(request, 'PollsApp/home/index.html')




def contacts(request):
    return shortcut.render(request, "PollsApp/survey/survey.html")


def signup(request: HttpRequest):


    if request.user.is_authenticated:
        request.session["Authenticated_Message"] = "You are already authenticated! There's no need to signin again 😁"
        return shortcut.redirect("index")


    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)

            login(request, user)
            request.session['Authenticated_Message'] = 'Your account has been created successfully!'
            return shortcut.redirect('index')
        else:
            print("Form is not valid")
            print(form.errors)

    else:
        form = SignUpForm()

    
  
    return shortcut.render(
        request, 
        "PollsApp/signup/signup.html",

        {"form": form})



def login_func(request):
    request.session['errorlogin'] = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():


            authenticated_user = authenticate(
            email = form.cleaned_data.get("email"), 
            password = form.cleaned_data.get("password")
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return shortcut.render(request, 'PollsApp/home/index.html')
            else:
                request.session['errorlogin'] = "There is no matching account with this credentials!"
    else:
        form = LoginForm()

    return shortcut.render(
        request, 
        "PollsApp/Login/login.html",

        { 
            "form": form,

    
        }
        )


def logout_view(request: HttpRequest):

    logout(request)
    request.session['logout-message'] = "You have been logged out!"
    return shortcut.render(request, 'PollsApp/home/index.html')
    

@login_required
def user_profile(request): 
    
    return shortcut.render(request, 'PollsApp/user/user_profile.html')


def search_user(request: HttpRequest, pk):
    if request.user.is_authenticated:
        try:
            searched_user = user.objects.get(username_iexact=pk)  

        except ObjectDoesNotExist:
            raise Http404("No MyModel matches the given query.")
    else:
        request.session["Notification_error"] = "You need to log in to see this page!"
        return shortcut.redirect("signup")
    
