from django.urls import path  # Importing path to define URL patterns

from . import views  # Importing views from the current module (item app)

app_name = 'item'  # Define the app namespace for URL reversing (for the 'item' app)

urlpatterns = [
    # URL pattern for the list of items, mapped to the 'items' view
    path('', views.items, name='items'),
    
    # URL pattern for creating a new item, mapped to the 'new' view
    path('new/', views.new, name='new'),
    
    # URL pattern for viewing details of a specific item, using its primary key (pk)
    path('<int:pk>/', views.detail, name='detail'),
    
    # URL pattern for deleting a specific item, mapped to the 'delete' view (using pk)
    path('<int:pk>/delete/', views.delete, name='delete'),
    
    # URL pattern for editing a specific item, mapped to the 'edit' view (using pk)
    path('<int:pk>/edit/', views.edit, name='edit'),
]
