from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation

# View to start a new conversation about an item
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)  # Retrieve the item based on its primary key

    # Redirect if the current user is the creator of the item
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # Check if there is already an existing conversation about this item
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    # If a conversation already exists, redirect to the first one
    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    # If the request method is POST, handle the form submission
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        # If the form is valid, create a new conversation and message
        if form.is_valid():
            # Create the new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)  # Add the current user to the conversation
            conversation.members.add(item.created_by)  # Add the item's creator to the conversation
            conversation.save()

            # Create and save the message associated with the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)  # Redirect to the item's detail page
    else:
        form = ConversationMessageForm()  # Instantiate the form for GET request
    
    # Render the template for starting a new conversation
    return render(request, 'conversation/new.html', {
        'form': form  # Pass the form to the template
    })

# View to display the inbox with all the user's conversations
@login_required
def inbox(request):
    # Get all conversations that the current user is a member of
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    # Render the inbox template with the conversations
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations  # Pass the conversations to the template
    })

# View to display the details of a specific conversation
@login_required
def detail(request, pk):
    # Get the conversation based on its primary key, ensuring the user is a member
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    # If the request method is POST, handle the form submission for a new message
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        # If the form is valid, save the new message and update the conversation
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            # Save the conversation after adding the message
            conversation.save()

            return redirect('conversation:detail', pk=pk)  # Redirect to the same conversation's page
    else:
        form = ConversationMessageForm()  # Instantiate the form for GET request

    # Render the conversation detail template with the conversation and form
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,  # Pass the conversation to the template
        'form': form  # Pass the form to the template
    })
