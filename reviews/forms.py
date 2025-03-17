from django import forms
<<<<<<< HEAD
from .models import Review # Import the Review model from models.py

# class ReviewForm(forms.Form):
#     user_name = forms.CharField( label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a name no longer than 100 characters!"
#     })

#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea,max_length=100) # Add a review_text field to the form
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5) # Add a rating field to the form

class ReviewForm(forms.ModelForm): # Change the form to a ModelForm
    class Meta: 
        model = Review
        fields = '__all__' # Use all fields from the Review model
        
        labels = { # Change the labels of the fields
            'user_name': 'Your Name', 
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }
        error_messages = { # Change the error messages for the fields
            'user_name': { # Change the error messages for the user_name field
                'required': "Your name must not be empty",
                'max_length': "Please enter a name no longer than 100 characters!"
            }
        }
=======


class ReviewForm(forms.Form):
    user_name = forms.CharField( label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a name no longer than 100 characters!"
    })

    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea,max_length=100) # Add a review_text field to the form
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5) # Add a rating field to the form
>>>>>>> dbfc25df7b5bee0a3e1ec8371757d327e1146584
