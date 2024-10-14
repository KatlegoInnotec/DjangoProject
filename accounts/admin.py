from django.contrib import admin
from .models import Comment, Topic,Article
# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Article)
class ArticelAdmin(admin.ModelAdmin):
    pass