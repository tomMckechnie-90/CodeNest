from . import views 
from django.urls import path

urlpatterns = [
    path("", views.index, name='home'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
]