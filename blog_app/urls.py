from django.urls import path

from . import views
from .views import AboutView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),
    path('about/', AboutView.as_view(), name='blog_about'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('scrape/', views.scrape_nltimes, name='scrape-nltimes'),
    path('upload/', views.upload_data, name='upload-data')
]
