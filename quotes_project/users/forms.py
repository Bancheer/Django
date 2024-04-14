from django import forms
from quotes.models import Quote, Author
from django.contrib.auth.forms import UserCreationForm 

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname']