from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from App_Login.models import Follow
from django.shortcuts import render,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posts,Like
from django.urls import reverse




# Create your views here.


@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user)
    posts=Posts.objects.filter(author__in=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    if request.method=='GET':
        search=request.GET.get('search','')
        result=User.objects.filter(username__icontains=search)
        return render(request,'App_Posts/Home.html',context={'search':search,'result':result,'posts':posts,'liked_posts':liked_post_list})
    
    
@login_required
def liked(request,pk):
    post=Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
        return HttpResponseRedirect(reverse('App_Posts:index'))
    
@login_required
def unliked(request,pk):
    post=Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Posts:index'))
    