from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    username = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        print(self.cleaned_data)
        email = self.cleaned_data['username'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['username'],
                password=self.cleaned_data['password1']
        )
        return user


class ImageForm(forms.ModelForm):
    user_image = forms.ImageField(label='user_image')

    class Meta:
        model = UserProfile
        fields = {'user_image'}
        widgets = {
            'image': forms.ImageField
        }


class CustomCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'user_image', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name...',
                'size': 13
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name...',
                'size': 13
            }),
            'date_of_birth': forms.DateInput(
                    format='%YYYY-%MM-%DD',
                    attrs={
                        'firstDay': 1,
                        'type': 'date',
                        'pattern': '\d{4}-\d{2}-\d{2}',
                        'lang': 'pl',
                        'format': 'yyyy-mm-dd'
                    }
            ),
            'city': forms.TextInput(attrs={
                'placeholder': 'City',
                'size': 7,
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'State',
                'size': 7,
            }),
            'zipcode': forms.TextInput(attrs={
                'placeholder': 'Zip',
                'size': 7,
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'size': 10
            }),
            'email_notification_active': forms.CheckboxInput(attrs={
                'vertical-align': 'middle'
            })
        }
