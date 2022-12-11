from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Feedback
from datetime import datetime
from .forms import PostForm, FeedbackForm, FeedbackPostForm
from django.utils import timezone
from django.http import HttpResponse
from django.core.mail import get_connection, send_mail
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.


# url route = index
def index(request):
    posts = Post.objects.filter(published_at__lte=datetime.now()).order_by('-published_at')
    return render(request,'blog/index.html',{'posts': posts})


class Success(TemplateView):
    template_name = "blog/success.html"

# url route = detail
def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/detail.html',{'post':post})


#url route = new-form
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/new_form.html',{'form':form})



#url route = update
def update_form(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/new_form.html',{'form':form})



#New feedback form
def feedback(request):
    if request.method == 'POST':
        feedForm = FeedbackForm(request.POST)
        if feedForm.is_valid():
            feed = feedForm.save(commit=False)
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
            feed.name,
            feed.feedback,
            feed.email,
            ['siteowner@email.com'],
            connection=con
            )
            feed.save()
            return redirect(reverse_lazy('success'))
            
            #return render(request,'blog/submitted.html',{'message':'Thank you for your feedback.'})
    else:
        feedForm = FeedbackForm()
    return render(request,'blog/feedback.html',{'form':feedForm})


#New feedback post form
def feedback_against_post(request, pk):
    post_to_be_saved_against = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        feedPostForm = FeedbackPostForm(request.POST  )
        if feedPostForm.is_valid():
            feed = feedPostForm.save(commit=False)
            feed.name = request.user
            feed.post = post_to_be_saved_against
            feed.save()
            return redirect(reverse_lazy('success'))
            #return render(request,'blog/submitted.html',{'message':'Thank you for your feedback.'})
    else:
        feedPostForm = FeedbackPostForm()
    return render(request,'blog/feedback.html',{'form':feedPostForm})


#Delete view, pass the id to delete it.
def PostDeleteView(request):
    try:

        pkey = request.GET.get('post_to_delete')
        #print(pkey)
        post = get_object_or_404(Post, pk=pkey)
        post.delete()
        return JsonResponse({'Deleted':True}, status = 200)
    except:
        return JsonResponse({"Deleted":False}, status=400)