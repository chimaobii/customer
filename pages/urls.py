from django.urls import path
from pages import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('create', views.create, name='create'),
    path('add', views.add, name='add'),
    path('profile/<int:id>',views.profile, name='profile'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]
