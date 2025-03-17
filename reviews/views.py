from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
# Create your views here.

def review(request):
    if request.method == "POST": # If the form has been submitted...
        entered_username = request.POST['username'] # Get the username from the POST request
        
        if entered_username == "":
            return render(request, 'reviews/review.html', { # Render the review page with an error message
                'error': True
            })
        print(entered_username)
        return HttpResponseRedirect('/thank-you') # Redirect to thank-you page
    
    return render(request, 'reviews/review.html', {
        'error': False 
    }) # Render the review page


def thank_you(request):
    return render(request, 'reviews/thank_you.html') # Render the thank-you page