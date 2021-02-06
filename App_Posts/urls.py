from django.urls import path
from . import views

app_name='App_Posts'


urlpatterns=[
    path('',views.home,name='index'),
    path('like/<pk>',views.liked,name='like'),
    path('unlike/<pk>',views.unliked,name='unlike'),
]
