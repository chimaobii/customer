from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.register, name= 'register'),
    path('signin', views.signin, name= 'signin'),
    path('profile', views.profile, name= 'profile'),
    path('signout', views.signout, name= 'signout'),
]