from django.shortcuts import render,redirect
from .forms import NewPostForm,UserForm,ProfileForm,ProfilePicForm,CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Tags,Follow,Comments
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from liked.models import Like

@login_required(login_url = '/accounts/login/')
def timeline(request):
	#profile section 
	try:
		current_user = request.user

		current_user_profile = current_user.profile

		profiles = Profile.retrieve_other_profiles(current_user.id)
	
	except objectDoesNotExist:
		raise Http404()

	#follow section 
	current_user = request.user

	following = Follow.retrieve_following(current_user.id)#get following profiles 

	posts = Post.retrieve_posts()#get all posts 

	following_posts = []#empty array that will be for posts or the profiles you follow

	for follow in following:

		for post in posts:

			if follow.profile == post.profile:

				following_posts.append(post)

	return render(request, 'timeline.html',{"profiles":profiles,"following":following,"user":current_user,"following_posts":following_posts})


@login_required(login_url = '/accounts/login/')
def profile(request):
	# profile_pic = ProfilePicForm()
	# if request.method == 'POST':
	# 	profile_pic = ProfilePicForm(instance=request.user)
	# 	if profile_pic.is_valid():
	# 		profile_pic.save()
	# current_user = request.user
	# current_profile = request.user.profile
	# if request.method == 'POST':
	# 	form = NewPostForm(request.POST,request.FILES)

	# 	if form.is_valid():
	# 		post = form.save(commit=False)#commit your post
	# 		post.user = current_user#post user should be current user
	# 		post.profile = current_profile#post should be saved to curent_user profile
	# 		post.save()#save the post 

	# 	elif comment_form.is_valid():
	# 		print('the comment form is working')

	# else:

	# 	form = NewPostForm()
	current_user = request.user

	if current_user.is_authenticated():#check to see if current user is authenticated
		print('Logged In')
		posts = Post.objects.filter(user=current_user)#get post by current user
		profile = Profile.objects.filter(user=current_user)#get specific profile

	tags = Tags.retrieve_tags()

	#follow section
	#follow section 
	current_user = request.user

	following = Follow.retrieve_following(current_user.id)#get following profiles 

	posts = Post.retrieve_posts()#get all posts 

	following_posts = []#empty array that will be for posts or the profiles you follow

	for follow in following:

		for post in posts:

			if follow.profile == post.profile:

				following_posts.append(post)


	return render(request, 'profile.html', {"posts":posts,"tags":tags,"profile":profile,"following":following,"user":current_user,"following_posts":following_posts})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):
	user = request.user

	if request.method == 'POST':
		profile_form = ProfileForm(request.POST, instance=request.user.profile, files=request.FILES)
	
		if profile_form.is_valid():
			profile_form.save()
			return redirect(profile)

	else:	

		profile_form = ProfileForm(instance=request.user.profile)

	return render(request, 'edit_profile.html',{"profile_form":profile_form,"user":user})

@login_required(login_url = '/accounts/login/')
def post(request):
	current_user = request.user
	current_profile = current_user.profile

	if request.method == 'POST':
		form = NewPostForm(request.POST,request.FILES)

		if form.is_valid():
			post = form.save(commit=False)#commit your post
			post.user = current_user#post user should be current user
			post.profile = current_profile#post should be saved to curent_user profile
			post.save()#save the post 

			return redirect(profile)

		elif comment_form.is_valid():
			print('the comment form is working')

	else:

		form = NewPostForm()

	return render(request, 'post.html', {"form":form,"current_user":current_user})

@login_required(login_url = '/accounts/login/')
def follow(request,id):
	current_user = request.user 

	follow_profile = Profile.objects.get(id=id)

	following = Follow(user=current_user, profile=follow_profile)

	following.save()

	return redirect(suggestions)

@login_required(login_url = '/accounts/login/')
def suggestions(request):
	try:
		current_user = request.user

		current_user_profile = current_user.profile

		profiles = Profile.retrieve_other_profiles(current_user.id)
	
	except objectDoesNotExist:
		raise Http404()

	# following = Follow.retrieve_following(current_user.id)#get following profiles 

	# posts = Post.retrieve_posts()#get all posts 

	# following_posts = []#empty array that will be for posts or the profiles you follow

	# for follow in following:

	# 	for post in posts:

	# 		if follow.profile == post.profile:

	# 			following_posts.append(post)


	return render(request, 'all.html', {"profiles":profiles,"user":current_user})

@login_required(login_url = '/accounts/login/')
def like(request,pk):
	user = request.user
	current_post = Post.objects.get(pk=pk)
	post = Post.retrieve_single_post(pk)
	# user_id = user.id

	if user.is_authenticated:
		like = Like(content_object=post,user=user)#like the specific post
		like.save()#save the like
	return redirect(single_post,current_post.pk)

@login_required(login_url='/accounts/register')
def single_post(request,id):
	try:
		current_user = request.user
		current_post = Post.objects.get(id=id)
		comments = Comments.retrieve_post_comments(id)
		# no_of_likes = Likes.number_of_likes(post_id=id)
		# get_likes = Likes.retrieve_post_likes(post_id=id)
		like_count = current_post.likes.all().count()
	except ObjectDoesNotExist:
		raise Http404()

	return render(request, 'single_post.html', {"post":current_post,"comments":comments,"like_count":like_count})

@login_required(login_url='/accounts/register')
def comment(request,id):
	current_user = request.user
	current_post = Post.objects.get(id=id)

	form = CommentForm(request.POST)
	if request.method == 'POST':
		

		if form.is_valid():
			comment = form.save(commit=False)#useful for when you get most of your model data from a form but need to populate some null fields with non-form data(user,post)
			comment.user = current_user#non form data 
			comment.post = current_post#non form data 
			comment.save()

			return redirect(single_post,current_post.id)

		else:
			form = CommentForm()

	return render(request,'comment.html',{"form":form,"current_post":current_post})



