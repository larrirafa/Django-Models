from django.urls import path
from blog.views.home import home
from blog.views.post_view import PostView

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('posts/', PostView.as_view(), name='post_list'),
]
