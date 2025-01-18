from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
]