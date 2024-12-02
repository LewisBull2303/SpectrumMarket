from django.contrib.auth.decorators import login_required  # Importing login_required decorator to ensure user is authenticated
from django.db.models import Q  # Importing Q for complex queries (filtering with OR conditions)
from django.shortcuts import render, get_object_or_404, redirect  # Importing helpers for rendering templates, fetching objects, and redirecting

from .forms import NewItemForm, EditItemForm  # Importing the forms for creating and editing items
from .models import Category, Item  # Importing Category and Item models

def items(request):
    query = request.GET.get('query', '')  # Retrieving search query from GET parameters
    category_id = request.GET.get('category', 0)  # Retrieving category filter from GET parameters
    categories = Category.objects.all()  # Fetching all categories to display in the filter
    items = Item.objects.filter(is_sold=False)  # Initially, fetch items that are not sold

    if category_id:  # If a category filter is applied
        items = items.filter(category_id=category_id)  # Filtering items by selected category

    if query:  # If a search query is provided
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))  # Filtering items by query in name or description

    return render(request, 'item/items.html', {  # Rendering the items list page
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)  # Passing the selected category ID to the template
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)  # Fetching the item by primary key (or 404 if not found)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]  # Fetching related items from the same category excluding the current item

    return render(request, 'item/detail.html', {  # Rendering the item detail page with related items
        'item': item,
        'related_items': related_items
    })

@login_required  # Ensures that only authenticated users can access this view
def new(request):
    if request.method == 'POST':  # If the form is submitted
        form = NewItemForm(request.POST, request.FILES)  # Creating form instance with POST data and files (image)

        if form.is_valid():  # If the form is valid
            item = form.save(commit=False)  # Creating the item instance but not saving yet
            item.created_by = request.user  # Setting the user who created the item
            item.save()  # Saving the item to the database

            return redirect('item:detail', pk=item.id)  # Redirecting to the newly created item's detail page
    else:
        form = NewItemForm()  # Creating an empty form instance for GET requests

    return render(request, 'item/form.html', {  # Rendering the form page for creating a new item
        'form': form,
        'title': 'New item',  # Title for the form page
    })

@login_required  # Ensures that only authenticated users can access this view
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)  # Fetching the item by primary key and ensuring the logged-in user is the creator

    if request.method == 'POST':  # If the form is submitted
        form = EditItemForm(request.POST, request.FILES, instance=item)  # Creating form instance with the item data to edit

        if form.is_valid():  # If the form is valid
            form.save()  # Saving the changes to the item

            return redirect('item:detail', pk=item.id)  # Redirecting to the item's detail page after editing
    else:
        form = EditItemForm(instance=item)  # Creating a form pre-populated with the existing item data

    return render(request, 'item/form.html', {  # Rendering the form page for editing the item
        'form': form,
        'title': 'Edit item',  # Title for the form page
    })

@login_required  # Ensures that only authenticated users can access this view
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)  # Fetching the item by primary key and ensuring the logged-in user is the creator
    item.delete()  # Deleting the item

    return redirect('dashboard:index')  # Redirecting to the dashboard after deletion
