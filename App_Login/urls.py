from django.urls import path
from . import views

app_name='App_Login'


urlpatterns=[
    path('',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('edit/',views.edit_profile,name='edit'),
    path('logout/',views.logout_user,name='logout'),
    path('user/',views.user_profile,name='user'),
    path('visit_user/<username>',views.visit_user_profile,name='visit_user'),
    path('follow/<username>',views.follow,name='follow'),
    path('unfollow/<username>',views.unfollow,name='unfollow'),
]
