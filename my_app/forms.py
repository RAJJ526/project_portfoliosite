from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')


from django import forms
from .models import Students
class Studentsform(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"


from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
