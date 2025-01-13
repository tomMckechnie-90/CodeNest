from . import views 
from django.urls import path

urlpatterns = [
    path("", views.index, name='home'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
]