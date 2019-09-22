from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        ]


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email',
        ]

class ProfileUpdateForm(forms.ModelForm):

    bio = forms.CharField(
        widget=TinyMCE(attrs={
            'required': False,
            'cols': 30,
            'rows': 10
        }))

    BIRTH_YEAR_CHOICES = range(1950,datetime.now().year +1)
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput)
    Date_Of_Birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),input_formats=['%Y-%m-%d'],help_text='Format:YYYY-MM-DD')
    Gender = forms.ChoiceField(widget=forms.RadioSelect,choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    class Meta:
        model = Profile
        fields = [
            'bio', 'profile_pic', 'Date_Of_Birth', 'Address', 'location', 'Gender'
        ]
