from django.urls import path
from .views import PostsList, PostList, PostsCreateView
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, upgrade_me



urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostList.as_view(), name='post'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name='upgrade'),
]

