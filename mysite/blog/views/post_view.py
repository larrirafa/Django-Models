from django.http import JsonResponse
from django.views import View
from blog.models import Post

class PostView(View):
    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.values("id", "title", "content"))
        return JsonResponse({"posts": posts})
