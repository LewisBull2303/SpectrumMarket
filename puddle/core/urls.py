from django.contrib.auth import views as auth_views  # Importing the built-in Django authentication views
from django.urls import path  # Importing path for URL routing

from . import views  # Importing views from the current module (core app)
from .forms import LoginForm  # Importing the custom LoginForm

app_name = 'core'  # Define the app namespace for URL reversing

urlpatterns = [
    # URL pattern for the homepage, mapped to the 'index' view
    path('', views.index, name='index'),
    
    # URL pattern for the contact page, mapped to the 'contact' view
    path('contact/', views.contact, name='contact'),
    
    # URL pattern for the signup page, mapped to the 'signup' view
    path('signup/', views.signup, name='signup'),
    
    # URL pattern for the login page, using Django's built-in LoginView with a custom login form
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
