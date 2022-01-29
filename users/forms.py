from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from users.models import ProfileModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # help_texts = {
        #     'username': '',
        #     'email': '',
        #     'password1': '',
        #     'password2': '',
        # }

    # This method for deleting helper texts work perfect
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'email', 'password1']:
            self.fields[field_name].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for field_name in ['username', 'email']:
            self.fields[field_name].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']
