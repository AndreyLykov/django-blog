from django.contrib import admin
from models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','publication_date', 'update_date')
    

admin.site.register(BlogPost)