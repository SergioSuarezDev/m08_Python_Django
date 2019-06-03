"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from posts.api import PostsAPI, PostDetailAPI
from posts.views import NewPostView, PostDetailView, LatestPostsView
from users.api import UsersAPI, UserDetailAPI, BlogsAPI, UserBlogAPI
from users.views import LogoutView, LoginView, BlogListView, SignUpView, BlogView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Website
    path('', LatestPostsView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('posts/new/', NewPostView.as_view(), name='new_post'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/<str:username>/', BlogView.as_view(), name='user_blog'),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),


    # API REST
    path('api/v1.0/users/', UsersAPI.as_view(), name='users_api'),
    path('api/v1.0/users/<int:pk>', UserDetailAPI.as_view(), name='user_detail'),
    path('api/v1.0/posts/<int:pk>', PostDetailAPI.as_view(), name='post_detail_api'),
    path('api/v1.0/posts/', PostsAPI.as_view(), name='posts_api'),
    path('api/v1.0/blogs/', BlogsAPI.as_view(), name='blogs_api'),
    path('api/v1.0/blogs/<str:username>', UserBlogAPI.as_view(), name='user_blog_api')

]
