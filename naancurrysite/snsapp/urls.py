from django.urls import path
from . import views

app_name = "snsapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mypost/<int:pk>', views.MyPostView.as_view(), name='mypost'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('like-home/<int:pk>', views.LikeHomeView.as_view(), name='like-home'),
    path('like-following/<int:pk>', views.LikeFollowingView.as_view(), name='like-following'),
    path('like-detail/<int:pk>', views.LikeDetailView.as_view(), name='like-detail'),
    path('follow-home/<int:pk>', views.FollowHomeView.as_view(), name='follow-home'),
    path('follow-detail/<int:pk>', views.FollowDetailView.as_view(), name='follow-detail'),
    path('follow-list/', views.FollowListView.as_view(), name='follow-list'),
]