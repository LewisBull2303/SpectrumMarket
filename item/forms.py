from django import forms  # Importing Django's forms module to create form classes
from .models import Item  # Importing the Item model to define forms for Item-related data

# Defining a shared CSS class for form input fields to maintain consistent styling
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

# Form for creating a new item
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item  # The model associated with this form is the Item model
        fields = ('category', 'name', 'description', 'price', 'image', )  # Fields included in the form
        widgets = {
            'category': forms.Select(attrs={  # Widget for the 'category' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={  # Widget for the 'name' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={  # Widget for the 'description' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={  # Widget for the 'price' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={  # Widget for the 'image' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            })
        }

# Form for editing an existing item
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item  # The model associated with this form is also the Item model
        fields = ('name', 'description', 'price', 'image', 'is_sold')  # Fields included in the form
        widgets = {
            'name': forms.TextInput(attrs={  # Widget for the 'name' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={  # Widget for the 'description' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={  # Widget for the 'price' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={  # Widget for the 'image' field, styled with INPUT_CLASSES
                'class': INPUT_CLASSES
            })
        }
