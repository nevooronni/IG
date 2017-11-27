from django import forms 
from django.contrib.auth.models import User
from .models import Profile,Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('photo',)

class ProfilePicForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=('profile_pic',)