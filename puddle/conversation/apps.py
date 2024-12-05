# Import the AppConfig class from django.apps to configure the app
from django.apps import AppConfig

# Define the configuration class for the 'conversation' app
class ConversationConfig(AppConfig):
    # Specify the default auto field type to use for auto-incrementing primary keys (BigAutoField)
    default_auto_field = 'django.db.models.BigAutoField'

    # Set the name of the app (which is 'conversation' in this case)
    name = 'conversation'
