from django import forms
from django.forms import ModelForm, Textarea
from .models import Contact
from .validators import validate_email_guest

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(
            required = True,
            label ="Name",
            widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'mb-3'})
        )
    
    
    email = forms.EmailField(
        required = True,
        label ="Email",
        widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'class': 'mb-3'}),
        validators=[validate_email_guest]
    )
    
    
    subject = forms.CharField(
        required = True,
        label ="Subject",
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'mb-3'})
    )
    
    message = forms.CharField(
        required = True,
        label ="Message", 
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        