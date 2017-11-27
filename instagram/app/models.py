from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save#define signals so our profile model auto created/updated when we create/update user instances.
from django.dispatch import receiver
import datetime as dt
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#USER Models
	bio = models.TextField(max_length=500, blank=True)
	website = models.CharField(max_length=30,blank=True)
	email = models.EmailField()
	phone_number = PhoneNumberField(max_length=10, blank=True)
	profile_pic = models.ImageField(upload_to = 'profile/', blank=True)
	
	def __str__(self):
		return self.user.username

	@classmethod
	def retrieve_profiles(cls):
		all_profiles = Profile.objects.all()
		return all_profiles

#hooking up the create_user_profile and save_user_profile methods to the User model wherever a save evernt occurs
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)#creates a profile when creating a user

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()#save a profile when saving a user


class Tags(models.Model):
	title = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.title
	class Meta:
		ordering = ['title']#ordering data everytime can be tedious meta subclass to specify model-specific options 

	def save_tag(self):
		self.save()

	def delete_tag(self):
		self.delete()

	@classmethod
	def retrieve_tags(cls):
		tags = Tags.objects.all()
		return tags

class Post(models.Model):
	post_time = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tags, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to = 'photos/')
	caption = models.TextField(blank=True)
	#likes = models.IntegerField()
	
	def __str__(self):
		return self.user.username
	class Meta:
		ordering = ['-post_time']#orders with the most recent at the top
	
	@classmethod
	def retrieve_profile_posts(cls,profile_id):
		prof_posts = Post.objects.filter(profile=profile_id).all()
		return prof_posts

	@classmethod
	def retrieve_posts(cls):
		posts = Post.objects.all()
		return posts