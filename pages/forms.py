from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'username'})
    )
    text = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'text'})
    )
