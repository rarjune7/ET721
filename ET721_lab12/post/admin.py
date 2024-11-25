from django.contrib import admin

# import the POST model 
from . models import Post

# Register your models here.
admin.site.register(Post)