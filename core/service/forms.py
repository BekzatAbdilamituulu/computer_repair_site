from django import forms
from .models import Contact, Client

class ContactForm(forms.ModelForm):
    model = Contact
    class Meta:
        model = Contact
        fields = ('name', 'last_name', 'email', 'phone', 'message')

        widgets = {
            'message': forms.Textarea(attrs={'cols': 35, 'rows': 7})
        }

class ClientForm(forms.ModelForm):
    model = Client
    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'message': forms.Textarea(attrs={'cols': 35, 'rows': 7})
        }
