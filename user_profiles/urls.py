from django.urls import path
from . import views


urlpatterns = [
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.view_profile, name='view_profile'),
]
