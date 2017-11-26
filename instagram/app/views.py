from django.http import HttpResponse#module and the class
import datetime as dt
from django.shortcuts import render,redirect

def post_of_today(request):
	# date = dt.date.today()#get current date

	return render(request, 'all-app/index.html')
