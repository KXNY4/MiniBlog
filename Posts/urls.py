from django.urls import include, path

from Posts.views import PostDeleteView, PostsCreateView, PostDetailView, PostsListView, PostsUserView
from PostsLike.views import ToggleLikeView

app_name = "posts"


urlpatterns = [
    path('home/', PostsListView.as_view(), name='home'),
    path('home/myposts', PostsUserView.as_view(), name='user'),
    path('home/create/', PostsCreateView.as_view(), name='create'),
    path('home/<slug:post_slug>/', PostDetailView.as_view(), name='detail'),
    path('home/<slug:post_slug>/like/', ToggleLikeView.as_view(), name='like'),
    path('home/<slug:post_slug>/delete/', PostDeleteView.as_view(), name='delete'),
]
