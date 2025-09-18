from django.views.generic import ListView
from ..models import Post

class PostView(ListView):
    model = Post
    template_name = "blog/home.html"  # crie esse template em blog/templates/blog/home.html
    context_object_name = "posts"
