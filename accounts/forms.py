from django import forms
from django.contrib.auth.forms import PasswordResetForm as PRF
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PasswordResetFormWithUsername(PRF):
	username = forms.CharField(
        label=_("Username"),
        max_length=254,
    )

	def get_users(self, email):
		username = self.cleaned_data['username']
		active_users = UserModel._default_manager.filter(**{
			'%s__iexact' % UserModel.get_email_field_name(): email,
			'is_active': True,
		})
		return (u for u in active_users if u.username == username)
		
				
