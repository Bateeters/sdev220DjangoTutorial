from django.contrib import admin
from .models import Post, Comment

# admin username: test123
# admin password: password1

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
