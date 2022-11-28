from django import forms
from .models import Post, Feedback, FeedbackPost

class PostForm(forms.ModelForm):
    """
    Model form, based on Post model, with title and text fields being the only editable ones.
    
    """
    class Meta:
        model = Post 
        fields = ("title",'text')


#Feedback form

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ("name",'email','feedback',)

#Feedback against Post
class FeedbackPostForm(forms.ModelForm):
    
    class Meta:
        model = FeedbackPost
        fields = ("reviewer",'email','feedback',)