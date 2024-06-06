from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    model = Contact
    class Meta:
        model = Contact
        fields = ('name', 'last_name', 'email', 'phone', 'message')

        widgets = {
            'message': forms.Textarea(attrs={'cols': 35, 'rows': 7})
        }
