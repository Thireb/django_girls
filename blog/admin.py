from django.contrib import admin
from .models import Post, Feedback, FeedbackPost


# Register your models here.
admin.site.register(Post)
# admin.site.register(FeedbackPost)#registered model
admin.site.register(Feedback)