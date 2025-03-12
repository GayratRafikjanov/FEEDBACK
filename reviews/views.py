from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def review(request):
    if request.method == "POST": # If the form has been submitted...
        entered_username = request.POST['username'] # Get the username from the POST request
        print(entered_username)
        return HttpResponseRedirect('/thank-you') # Redirect to thank-you page
    return render(request, 'reviews/review.html') # Render the review page


def thank_you(request):
    return render(request, 'reviews/thank_you.html')