from django.contrib.auth.models import User  # Importing the built-in User model from Django's auth system
from django.db import models  # Importing the models module for defining database models

class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=255)  # Field for the category name, up to 255 characters

    class Meta:
        # Define default ordering of categories (alphabetically by name) and set a custom plural name for the category
        ordering = ('name',)  # Ordering categories by the name field
        verbose_name_plural = 'Categories'  # Custom plural name for the Category model
    
    def __str__(self):
        """Return the category name when displaying the model instance."""
        return self.name


class Item(models.Model):
    """Model representing an item for sale."""
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)  # Foreign key to Category, one-to-many relation
    name = models.CharField(max_length=255)  # Item name, up to 255 characters
    description = models.TextField(blank=True, null=True)  # Optional description for the item
    price = models.FloatField()  # Price of the item as a float value
    image = models.ImageField(upload_to='item_images', blank=True, null=True)  # Optional image for the item (uploaded to 'item_images' directory)
    is_sold = models.BooleanField(default=False)  # Boolean field to indicate if the item is sold or not (defaults to False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  # Foreign key to the User who created the item
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp indicating when the item was created, auto-filled on creation
    
    def __str__(self):
        """Return the item name when displaying the model instance."""
        return self.name
