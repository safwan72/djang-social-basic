from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    post_image=forms.ImageField(label='Attach A Photo')
    caption=forms.CharField(label='Whats On Your Mind?',widget=forms.Textarea())
    class Meta:
        model=Posts
        fields=['post_image','caption',]