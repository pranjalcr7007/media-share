from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostDetailViewu, 
    PostCreateView,
    PostCreateViewu,
    PostUpdateView,
    PostUpdateViewu,
    PostDeleteView,
    PostDeleteViewu,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('postu/<int:pk>/', PostDetailViewu.as_view(), name='post-detailu'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/newu/', PostCreateViewu.as_view(), name='post-createu'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/updateu/', PostUpdateViewu.as_view(), name='post-updateu'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/deleteu/', PostDeleteViewu.as_view(), name='post-deleteu'),
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
    path('about/', views.about, name='blog-about'),
]
