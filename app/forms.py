from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile,Post,Comments

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=('photo','caption',)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name',)		

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio','website','email','phone_number','photo','gender',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comment',)
