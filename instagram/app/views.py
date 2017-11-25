from django.http import HttpResponse#module and the class
import datetime as dt
from django.shortcuts import render,redirect

#create your views here.views
def welcome(request):#one argument which is the request contains information fo the current web request that has triggered this view must be the first paremeter of our view functions instance of the django.http.HttpResponse class 
	date = dt.date.today()#get current date

	return render(request, 'all-app/index.html', {"date":date})

# def post_of_today(request):
# 	date = dt.date.today()#get current date
	
# 	#function to convert date object to find specific day
# 	day = convert_dates(date)
# 	html = f'''
# 		<html>
# 			<body>
# 				<h1>instagram</h1>
# 				<p>{day} {date.day}-{date.month}-{date.year}</p>
# 			</body>
# 		</html>
# 					'''
# 	return HttpResponse(html)