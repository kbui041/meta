from django import forms
from .models import Review

# Form class for the Review model
class ReviewForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = Review
        # Define the fields to include in the form
        fields = ['comment', 'rating']
