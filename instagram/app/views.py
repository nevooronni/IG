from django.http import HttpResponse#module and the class

#create your views here.views
def welcome(request):
	return HttpResponse('Welcome to the instagram app')
