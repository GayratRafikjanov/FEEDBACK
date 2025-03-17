from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
# Create your views here.

def review(request):
    if request.method == "POST": # If the form has been submitted...
        form = ReviewForm(request.POST) # A form bound to the POST data
        
        if form.is_valid():
            review = Review(
              user_name=form.cleaned_data['user_name'], # Get the user_name from the form
              review_text=form.cleaned_data['review_text'], # Get the review_text from the form
              rating=form.cleaned_data['rating'], # Get the rating from the form
           )
            review.save() # Save the review to the database
            return HttpResponseRedirect('/thank-you') # Redirect to thank-you page
    else:
        form = ReviewForm() # An unbound form
                            # Render the review page with the form

    return render(request, 'reviews/review.html', {
        'form': form # Pass the form object to the template
    }) # Render the review page


def thank_you(request):
    return render(request, 'reviews/thank_you.html') # Render the thank-you page