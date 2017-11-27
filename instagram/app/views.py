from django.shortcuts import render

def timeline(request):
    return render(request, 'timeline.html')

# def timeline(request):
# 	current_user = request.user
# 	if request.method == 'POST':
# 		form = NewPostForm(request.POST,request.FILES)

# 		if form.is_valid():
# 			post = form.save(commit=False)#commit your post
# 			post.user = current_user#save post to current user profile
# 			post.save()#save the post 

# 		elif comment_form.is_valid():
# 			print('the comment form is working')

# 	else:

# 		form = NewPostForm()


# 	return render(request,'all-app/timeline.html',{"form":form})		

# @login_required(login_url='/accounts/login/')
# def login(request):
# 	return render(request, 'index.html')

# @login_required(login_url='/accounts/register/')
# def register(request):
# 	return render(request, 'home.html')

# def profile(request):
# 		profile_pic = ProfilePicForm()
# 		if request.method == 'POST':
# 			profile_pic = ProfilePicForm(instance=request.user)
# 			if profile_pic.is_valid():
# 				profile_pic.save()

# 		return render(request, 'profile.html', {"profile_pic":profile_pic})

