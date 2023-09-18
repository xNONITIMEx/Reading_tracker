from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from . models import Reader


class ReaderCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = Reader.objects.filter(email=email)
        if new.count():
            raise ValidationError('Email already exists')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        reader = Reader.objects.create_user(self.cleaned_data['email'],
                                            self.cleaned_data['password2'])
        return reader

    class Meta:
        model = Reader
        fields = ('email', 'password1', 'password2')


class ReaderChangeForm(UserChangeForm):
    class Meta:
        model = Reader
        fields = ('email',)


class ReaderLogInForm(AuthenticationForm):
    pass