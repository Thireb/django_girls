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
#Feedback against the whole site
class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ("name",'email','feedback',)
        
    def clean_email(self):
        mail = self.cleaned_data.get('email')
        if not mail.endswith('softcatalyst.com'):
            raise forms.ValidationError('Only softcatalyst.com emails are accepted.')
        return mail
    

#Feedback against one post
class FeedbackPostForm(forms.ModelForm):
    
    class Meta:
        model = FeedbackPost
        fields = ("name",'email','feedback',)
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('softcatalyst.com'):
            raise forms.ValidationError("Only softcatslyst emails are accepted.")
        return email