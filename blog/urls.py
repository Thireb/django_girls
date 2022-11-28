from django.urls import path
from . import views

""" 
    urls for index, detail, new-form, and update.
    
"""
urlpatterns = [
    
    
    
    path('',views.index, name='index'),
    path('post/<int:pk>/',views.detail,name='detail'),
    path('form/',views.new_post,name='new-form'),
    path('post/<int:pk>/update',views.update_form,name='update'),
    #feedback form
    path('feedback',views.feedback, name='feedback'),
    #feedback against a post
    path('post/<int:pk>/feedback',views.feedback_against_post, name='feedback_Post'),
    
]
'''
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAAxElEQVQ4je3UMWoCURCH8d+uFmqVLloLEa29gW0uYeEZ0ll4heAJkipVCkGwVK+hfYiw28R0YrEbUMEgu6/0a4Y3xff+DMwQmCivDTzjoaAnxQz7GBXM8VQiWCd3VKCHtxKyP97RjVHHPoDwB404gOiMu/AuLChM8RjA1UJSxQYJPvGFA8b4Rh+jG2RN7LCNTppt2bV5wRQrLDCRrdV/JNhC9aS5yWst/+0VH1jekPAqI9lM1xgWEUQX74Hspq3wWyZZMI6Q7SEbdUG5+wAAAABJRU5ErkJggg==">
'''