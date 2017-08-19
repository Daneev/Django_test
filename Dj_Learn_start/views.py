from django.shortcuts import render_to_response
from Dj_Learn_start.models import Post


def post_list(request):

    post_list = Post.objects.all()
    return render_to_response("blog/post_list.html", {"post_list": post_list})