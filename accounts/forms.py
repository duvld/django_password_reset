from django import forms
from django.contrib.auth.forms import PasswordResetForm as PRF
from django.utils.translation import gettext, gettext_lazy as _

class PasswordResetFormWithUsername(PRF):
	username = forms.CharField(
        label=_("Username"),
        max_length=254,
    )