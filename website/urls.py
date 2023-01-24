from django.urls import path, include
from . import views
from .models import Register

urlpatterns = [
    path('', views.page1),
    path('page1_.html', views.page1_),
    path('page2.html', views.page2),
    path('page3.html', views.page3),
    path('login.html', views.login),
    path('user_reg.html', views.user_reg),
]
