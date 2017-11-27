from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.timeline,name = 'timeline'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^profile/edit-profile',views.edit_profile,name = 'edit_profile'),
]
