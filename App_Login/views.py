from App_Posts.forms import PostForm
from .models import UserProfile,Follow
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,HttpResponseRedirect
from .forms import CreateNewUser,EditProfile
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def sign_up(request):
    form=CreateNewUser()
    registered=False
    if request.method=='POST':
        form=CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            user_profile=UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request,'App_Login/Signup.html',context={'form':form,'registered':registered,'title':'SIGNUP Page'})


def login_page(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Posts:index'))
    return render(request,'App_Login/Login.html',context={'title':'Login Page','form':form})
                
                
@login_required
def user_profile(request):
   form=PostForm()
   if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        return HttpResponseRedirect(reverse('App_Login:user'))
    
   return render(request,'App_Login/user.html',context={'form':form})           
                
                
@login_required
def edit_profile(request):
    current_user=UserProfile.objects.get(user=request.user)
    form=EditProfile(instance=current_user)
    
    if request.method=='POST':
        form=EditProfile(request.POST,request.FILES,instance=current_user)
        form.save(commit=True)
        form=EditProfile(instance=current_user)
        return HttpResponseRedirect(reverse('App_Login:user'))
    return render(request,'App_Login/profile.html',context={'form':form})



@login_required
def visit_user_profile(request,username):
   user_other=User.objects.get(username=username)
   already_followed=Follow.objects.filter(follower=request.user,following=user_other)
   if user_other==request.user:
       return HttpResponseRedirect(reverse('App_Login:user'))
   return render(request,'App_Login/Profile_visit.html',context={'user_other':user_other,'already_followed':already_followed})



@login_required
def follow(request,username):
   following_user=User.objects.get(username=username)
   follower_user=User.objects.get(username=request.user)
   already_followed=Follow.objects.filter(follower=follower_user,following=following_user)
   
   if not already_followed:
       followed_user=Follow(follower=follower_user,following=following_user)
       followed_user.save()
       return HttpResponseRedirect(reverse('App_Login:visit_user',kwargs={'username':username}))
   
   
@login_required
def unfollow(request,username):
   following_user=User.objects.get(username=username)
   follower_user=User.objects.get(username=request.user)
   already_followed=Follow.objects.filter(follower=follower_user,following=following_user)
   already_followed.delete()
   return HttpResponseRedirect(reverse('App_Login:visit_user',kwargs={'username':username}))
   
   


@login_required
def logout_user(request):
   logout(request)
   return HttpResponseRedirect(reverse('App_Login:login'))



