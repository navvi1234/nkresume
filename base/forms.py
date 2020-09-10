from django import forms
from django.contrib.auth.models import User
#from base.models import employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


#from apps.userprofile.models import Profile

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
class dataform(forms.Form):
    age=forms.IntegerField()
    resting_Blood_Pressure=forms.IntegerField()
    cholesterol=forms.IntegerField()
    max_heart_rate_achieved=forms.IntegerField()
    exercise_relative_to_rest_Oldpeak=forms.FloatField()

class SignInForm(AuthenticationForm):
    class meta:
        model=User
        fields = [
            'username',
            'password',
            ]
