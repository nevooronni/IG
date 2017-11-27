from django.shortcuts import render
from .forms import NewPostForm,UserForm,ProfileForm
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/accounts/login/')
def timeline(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewPostForm(request.POST,request.FILES)

		if form.is_valid():
			post = form.save(commit=False)#commit your post
			post.user = current_user#save post to current user profile
			post.save()#save the post 

		elif comment_form.is_valid():
			print('the comment form is working')

	else:

		form = NewPostForm()

	return render(request, 'timeline.html',{"form":form})



def profile(request):
	# profile_pic = ProfilePicForm()
	# if request.method == 'POST':
	# 	profile_pic = ProfilePicForm(instance=request.user)
	# 	if profile_pic.is_valid():
	# 		profile_pic.save()

	return render(request, 'profile.html')

def edit_profile(request):
	user_form = UserForm(instance=request.user)#get form
	profile_form = ProfileForm(instance=request.user.profile)

	return render(request, 'edit_profile.html',{"user_form":user_form,"profile_form":profile_form})
