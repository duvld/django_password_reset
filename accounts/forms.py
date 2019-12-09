from django import forms
from django.contrib.auth.forms import PasswordResetForm as PRF
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PasswordResetFormWithUsername(PRF):
	username = forms.CharField(
        label=_("Username"),
        max_length=254,
        required=False,
    )

    # def __init__(self, *args, **kwargs):
    # 	 super().__init__(*args, **kwargs)
    # 	 print(self)
    # 	 print('###')
    # 	 print(self.username)
    # 	 print('##done##')
    	

	def get_users(self, email):
		username = self.cleaned_data['username']
		active_users = UserModel._default_manager.filter(**{
			'%s__iexact' % UserModel.get_email_field_name(): email,
			'is_active': True,
		})
		print('--------')
		print(active_users)
		print('--------')
		print(username)
		print('--------')
		if(username == ""):
			return(u for u in active_users if u.has_usable_password())
		else:
			return (u for u in active_users if u.username == username)
				
