from django.shortcuts import render_to_response
from Dj_Learn_start.models import Post


def post_list(request):
    post_list = Post.objects.all()

    query = request.GET.get("query")
    if query:
        post_list = post_list.filter(text__icontains=query)

    return render_to_response("blog/post_list.html", {"post_list": post_list, "query": query})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render_to_response("blog/post_detail.html", {"post": post})

def test(request):
    return render_to_response("blog/test.html")




