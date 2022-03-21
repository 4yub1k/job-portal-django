from django.urls import path
from . import views

urlpatterns = [
    path('',views.apply,name='apply'), #future use of apply form
]

    
