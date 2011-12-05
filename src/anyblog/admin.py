import models
from django.contrib import admin

class BlogPostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'author')


admin.site.register(models.BlogPost, BlogPostAdmin)