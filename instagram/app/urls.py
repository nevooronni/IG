from django.conf.urls import url#import url function 
from . import views#import views module

urlpatterns=[
	url('^$',views.welcome,name = 'welcome')
]#list of url instances for our app which have a regular experession,view,kwargs,name(last two are optional)