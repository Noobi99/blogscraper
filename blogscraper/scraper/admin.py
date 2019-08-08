from django.contrib import admin
from .models import Blog, BlogPost

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    pass
class BlogPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)