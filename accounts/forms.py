from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserType, CompanyInfo, UserInfo

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserTypeForm(forms.ModelForm):

    class Meta:
        # the model
        model = UserType 
        exclude = ('isCompany', 'user', )

class CompanyInfoForm(forms.ModelForm):

    class Meta:
        # the model
        model = CompanyInfo
        # user is not visible
        exclude = ('user',)

class UserInfoForm(forms.ModelForm):

    class Meta:
        # the model
        model = UserInfo
        # user is not visible
        exclude = ('user',)

