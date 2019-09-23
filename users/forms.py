from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = [
            'first_name','last_name' , 'email', 'mobile', 'gender', 'address', 'city', 'state',
            'country','profile_pic','password1', 'password2','role','supervisor',
        ]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = CustomUser
        fields = ['first_name','last_name','email', 'mobile', 'gender', 'address', 'city', 'state',
                  'country','profile_pic',
        ]
