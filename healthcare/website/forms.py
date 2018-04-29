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


class Profile(forms.Form):
    name = forms.TextField(required = True)    
    address = forms.TextField(required = True)
    dob = forms.TextField(required = True)
    encr_key = forms.TextField(required = True)
    encr_key_confirm = forms.TextField(required = True)


