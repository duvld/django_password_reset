from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext, gettext_lazy as _

class PasswordResetFormWithUsername(PasswordResetForm):
	email = forms.CharField(
        label=_("Username"),
        max_length=254,
    )