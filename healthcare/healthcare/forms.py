from django import forms
from django.contrib.auth import login, logout, authenticate
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator, MinValueValidator, \
RegexValidator, URLValidator

from django.contrib.auth.models import User


from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator, MinValueValidator, \
RegexValidator, URLValidator
from django.template.defaultfilters import filesizeformat



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username is None or password is None:
            raise forms.ValidationError("Invalid username or password")
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("Invalid username or password")
        if not user.is_active:
            raise forms.ValidationError("User is blocked")
        cleaned_data['user'] = user
        return cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(
        label = _("Username"),
        max_length = 30,
        widget = forms.TextInput(),
        required = True,
        validators = [
        RegexValidator(
            regex = '^[a-zA-Z0-9-_+.]*$',
            message = 'Username required. 30 characters or fewer. \
            Letters, digits and @/./+/-/_ only.',
            code = 'invalid_username'
        ),
        ]
    )
    password = forms.CharField(
        label = _("Password"),
        widget = forms.PasswordInput(render_value=False),
        min_length = 8,
    )

    password_confirm = forms.CharField(
        label = _("Password (again)"),
        widget = forms.PasswordInput(render_value=False),
        min_length = 8,
    )
    email = forms.EmailField(
        label = _("Email"),
        widget = forms.TextInput(),
        required=True
    )


    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
            raise forms.ValidationError("This username has already existed.")
        except User.DoesNotExist:
            pass

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
            raise forms.ValidationError("This email is already taken.")
        except User.DoesNotExist:
            pass

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm != password :
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data
