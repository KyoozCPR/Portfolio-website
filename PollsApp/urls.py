from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('input/', views.survey, name='survey'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_func, name="login"),
    path('thanks/', views.greeting, name='thankyoupage'),
    path('user/<str:pk>', views.search_user, name='userquery')
]   


