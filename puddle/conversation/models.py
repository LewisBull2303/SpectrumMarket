from django.contrib.auth.models import User  # Importing the User model for user-related functionality
from django.db import models  # Importing Django's models module to define database models

from item.models import Item  # Importing the Item model to establish a relationship with conversations

class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)  
    # A conversation is linked to an Item, a user can have conversations related to a specific item.

    members = models.ManyToManyField(User, related_name='conversations')  
    # Multiple users can be members of a conversation. Many-to-many relationship with the User model.

    created_at = models.DateTimeField(auto_now_add=True)  
    # Timestamp for when the conversation is created, automatically set to the current time when the object is created.

    modified_at = models.DateTimeField(auto_now=True)  
    # Timestamp for when the conversation was last modified, automatically updated whenever the object is modified.

    class Meta:
        ordering = ('-modified_at',)  
        # Orders conversations by the most recently modified conversations first.

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)  
    # Each message belongs to a specific conversation. This is a one-to-many relationship between Conversation and ConversationMessage.

    content = models.TextField()  
    # Content of the message, allowing longer text.

    created_at = models.DateTimeField(auto_now_add=True)  
    # Timestamp for when the message is created, automatically set to the current time when the message is created.

    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)  
    # A message is created by a user, linking back to the User model. Each message has an associated creator.
