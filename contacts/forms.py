from django import forms
from .models import Contact, Notes


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
            'notes'
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields  = [
            'note',
        ]