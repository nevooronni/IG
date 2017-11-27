from django import forms 
from django.contrib.auth.models import User
from .models import Profile,Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('photo',)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name',)		

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('bio','website','phone_number','email','profile_pic',)