from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()), # Change the path to an empty string
    path('thank-you', views.thank_you)
]
