from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField( label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a name no longer than 100 characters!"
    })

    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea,max_length=100) # Add a review_text field to the form
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5) # Add a rating field to the form