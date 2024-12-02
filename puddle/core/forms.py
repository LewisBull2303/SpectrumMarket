# Import necessary modules from Django for creating forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Define a form for user login, inheriting from Django's AuthenticationForm
class LoginForm(AuthenticationForm):
    # Define the username field with a custom widget for styling and placeholder text
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',  # Placeholder text
        'class': 'w-full py-4 px-6 rounded-xl'  # Custom CSS classes for styling
    }))
    # Define the password field with a custom widget for styling and placeholder text
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',  # Placeholder text
        'class': 'w-full py-4 px-6 rounded-xl'  # Custom CSS classes for styling
    }))

# Define a form for user sign-up, inheriting from Django's UserCreationForm
class SignupForm(UserCreationForm):
    # Meta class to specify the model and fields to be used in the form
    class Meta:
        model = User  # Use the User model for the form
        fields = ('username', 'email', 'password1', 'password2')  # Fields to be included in the form
    
    # Define the username field with a custom widget for styling and placeholder text
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',  # Placeholder text
        'class': 'w-full py-4 px-6 rounded-xl'  # Custom CSS classes for styling
    }))
    # Define the email field with a custom widget for styling and placeholder text
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',  # Placeholder text
        'class': 'w-full py-4 px-6 rounded-xl'  # Custom CSS classes for styling
    }))
    # Define the password1 field with a custom widget for styling and placeholder text
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',  # Placeholder text
        'class': 'w-full py-4 px-6 rounded-xl'  # Custom CSS classes for styling
    }))
    # Define the password2 field with a custom widget for styling and placeholder text
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',  # Placeholder text
        'class': 'w-full py-4 px-6 rounded-xl'  # Custom CSS classes for styling
    }))
