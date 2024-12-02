from django.contrib.auth.decorators import login_required  # Importing the login_required decorator to ensure the user is authenticated
from django.shortcuts import render, get_object_or_404  # Importing helpers for rendering templates and fetching objects

from item.models import Item  # Importing the Item model to fetch items related to the user

@login_required  # Ensures that only authenticated users can access this view
def index(request):
    items = Item.objects.filter(created_by=request.user)  # Fetching all items that were created by the currently logged-in user

    return render(request, 'dashboard/index.html', {  # Rendering the dashboard page, passing the user's items to the template
        'items': items,
    })
