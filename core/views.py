from django.shortcuts import render, redirect

from item.models import Category, Item  # Importing Category and Item models from the 'item' app

from .forms import SignupForm  # Importing the SignupForm from the forms module

def index(request):
    """View function for the homepage that displays items and categories."""
    # Fetch the first 6 unsold items to display on the homepage
    items = Item.objects.filter(is_sold=False)[0:6]
    # Fetch all categories to display in the homepage
    categories = Category.objects.all()

    # Render the 'index.html' template with the categories and items as context
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    """View function to render the contact page."""
    # Simply renders the 'contact.html' template
    return render(request, 'core/contact.html')

def signup(request):
    """View function to handle user registration."""
    if request.method == 'POST':
        form = SignupForm(request.POST)  # Initialize the SignupForm with POST data

        if form.is_valid():
            form.save()  # Save the new user if the form is valid

            return redirect('/login/')  # Redirect to the login page after successful signup
    else:
        form = SignupForm()  # Initialize an empty SignupForm for GET request

    # Render the 'signup.html' template, passing the form as context
    return render(request, 'core/signup.html', {
        'form': form
    })
