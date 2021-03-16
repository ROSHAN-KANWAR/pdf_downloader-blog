from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Blogpost
from django.core.exceptions import ValidationError
class Signupform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels={'first_name':'Enter Your Name','last_name':'Enter Your Last Name',
                'email':'Email Address'}

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
               'first_name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z]+'}),
               'last_name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z]+'}),
               'email': forms.EmailInput(attrs={'class': 'form-control'})}

##login

class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username']
        labels={'username':'user'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}
        label_suffix={'username':" - "}



##profile user

class profile_user(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active']
##admin profile

class profile_admin(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'


##blog create
class Blogcreate(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields=['img','title','dec','cat']
        labels = {'img': 'Select Image :', 'title':'Suitable Title :',
                  'dec':'Write Your Blog :','pdate':'Publish Date :','cat':'Writter Name :'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'cat': forms.TextInput(attrs={'class': 'form-control'}),
                   'dec': forms.Textarea(attrs={'class': 'form-control'})}
