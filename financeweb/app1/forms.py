from app1.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from app1.models import reminder


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('companyname',)


class reminderForm(forms.ModelForm):
	

	class Meta:
		model = reminder
		fields = ('title','description', 'date_created', 'date_to_remind','time_to_remind','active')        