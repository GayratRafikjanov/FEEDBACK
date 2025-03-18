from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View  # Import the View class from django.views
# Create your views here.

class ReviewView(View):
    
    def get(self, request): # Define a get method
        form = ReviewForm() # Create a form instance
        return render(request, "reviews/review.html", { # Render the review.html template
            "form": form # Pass the form to the template
        })
    
    
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        
        return render(request, "reviews/review.html", {
            "form": form
        })
    

def thank_you(request):
    return render(request, 'reviews/thank_you.html') # Render the thank-you page