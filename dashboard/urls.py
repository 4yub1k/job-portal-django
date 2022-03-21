from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('signin/',auth_views.LoginView.as_view(template_name='dashboard/login.html'),name='login'), #built in 
    path('signout/', auth_views.LogoutView.as_view(),name='logout'),#built in
]

    
