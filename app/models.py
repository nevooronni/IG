from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save#define signals so our profile model auto created/updated when we create/update user instances.
from django.dispatch import receiver
import datetime as dt
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Sum
# from vote.models import VoteModel#import vote model
# from vote.managers import VotableManager
from liked.models import Like
from django.contrib.contenttypes.fields import GenericRelation

#default images for profile
DEFAULT = 'profile/index.jpeg'

Genders_Choices = (
		('Female', 'female'),
		('Male', 'male'),
		('Both', 'both'),
		('None', 'non-specified'),
	)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#USER Models
	name = models.TextField(max_length=500, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	website = models.CharField(max_length=30,blank=True)
	email = models.EmailField()
	phone_number = PhoneNumberField(max_length=10, blank=True)
	photo = models.ImageField(upload_to = 'profile/',blank=True,default=False)
	gender = models.CharField(max_length=30,choices=Genders_Choices,default='None',blank=True)
	
	def __str__(self):
		return self.user.username

	# @classmethod
	# def one_profile(cls,id):
	# 	profile = Profile.objects.filter(user=user_id).all()
		
	@classmethod
	def retrieve_profiles(cls):
		all_profiles = Profile.objects.all().order_by('-id')
		return all_profiles

	@classmethod
	def retrieve_other_profiles(cls,user_id):
		profiles = Profile.objects.all()#get all profiles

		other_profiles = []#empty profile list

		for profile in profiles:

			if profile.user.id != user_id:#check if current profile user id is equal to parameter
				other_profiles.append(profile)

		return other_profiles#return all profiles

	@property
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):#return whether an object has an attribute with the same name
			return self.photo.url

#hooking up the create_user_profile and save_user_profile methods to the User model wherever a save evernt occurs
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)#creates a profile when creating a user

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()#save a profile when saving a user

@property 
def photo_url(self):
	if self.photo and hasattr(self.photo, 'url'):
		return self.photo.url	

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
	photo = models.ImageField(upload_to = 'photos/',blank=True,default=False)
	caption = models.TextField(blank=True)
	likes = GenericRelation(Like)
		# upvote_count = models.PositiveIntegerField(default=0)
	# like_remove_count = models.PositiveIntegerField(default=0)
	
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

	@classmethod
	def retrieve_single_post(cls,pk):
		post = cls.objects.get(pk=pk)
		return post

	@classmethod
	def retrieve_user_posts(cls,user_id):
		user_posts = Post.objects.filter(user=user_id).all()
		return user_posts

	@property 
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url	

class Follow(models.Model):
	user = models.ForeignKey(User)#defines the user
	profile = models.ForeignKey(Profile)#follow a profile

	def __str__(self):
		return self.user.username

	@classmethod
	def retrieve_following(cls,user_id):
		following = Follow.objects.filter(user=user_id).all()
		return following 

# class Likes(models.Model):
# 	user = models.ForeignKey(User,on_delete=models.CASCADE)#defines the user#cascaded deletes this objects when other related referenced objects are deleted too
# 	post = models.ForeignKey(Post,on_delete=models.CASCADE)#the post to like
# 	likes = models.PositiveIntegerField(null=True,blank = True)

# 	def __str__(self):
# 		return self.user.username

# 	@classmethod
# 	def retrieve_post_likes(cls,post_id):
# 		post_likes = Likes.objects.filter(post=post_id)
# 		return post_likes

# 	@classmethod
# 	def number_of_likes(cls,post_id):
# 		post = Likes.objects.filter(post=post_id)
# 		likes = post.aggregate(Sum('likes')).get('likes_sum',0)
# 		return likes

class Comments(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)#THE USER
	post = models.ForeignKey(Post,on_delete=models.CASCADE)#post with the comments
	comment = models.TextField(blank=True)

	def __str__(self):
		return self.user.username

	@classmethod
	def retrieve_post_comments(cls,post_id):
		post_comments = Comments.objects.filter(post=post_id)
		return post_comments
