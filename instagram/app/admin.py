from django.contrib import admin
from .models import Profile,Tags,Post

class PostAdmin(admin.ModelAdmin):
	filter_horizontal = ('tags',)#specify the property allows ordering of many to many fields and pass in the tags article field
	
admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Post,PostAdmin)
