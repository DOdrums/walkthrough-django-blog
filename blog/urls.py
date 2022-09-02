from . import views
from django.urls import path


urlpatterns = [
    path('', views.Postlist.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]