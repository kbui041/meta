from django import forms
from .models import Review, Booking

# Form class for the Review model
class ReviewForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = Review
        # Define the fields to include in the form
        fields = ['comment', 'rating']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5')
        return rating


class BookingForm (forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']