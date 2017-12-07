from django.conf.urls import url
from . import views
from django.conf import settings#IMPORT SETTINGS
from django.conf.urls.static import static#USE STATIC FILES

urlpatterns=[
    url('^$',views.timeline,name = 'timeline'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^profile/edit-profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^post/$',views.post,name = 'post'),
   	url(r'^follow/(\d+)', views.follow, name="follow"),
   	url(r'^all/$',views.suggestions,name = 'suggestions'),
   	url(r'^single_posts/(\d+)',views.single_post,name = 'single_post'),
		url(r'^like/(\d+)',views.like, name="like"),
		url(r'^comment/(\d+)',views.comment,name = "comment"),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
