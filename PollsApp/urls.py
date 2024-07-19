from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_func, name="login"),
    path('thanks/', views.greeting, name='thankyoupage'),
    path('user-profile', views.user_profile, name="user-profile"),
    path('user/<str:pk>', views.search_user, name='userquery')
]   


