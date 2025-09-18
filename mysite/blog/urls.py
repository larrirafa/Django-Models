from django.urls import path
from blog.views.post_view import PostView   # importa direto do arquivo

urlpatterns = [
    path('', PostView.as_view(), name='home'),
]
