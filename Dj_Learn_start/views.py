from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from .forms import OrderForm
from .models import Post, Comment


def post_list(request):
    post_list = Post.objects.all()

    query = request.GET.get("query")
    if query:
        post_list = post_list.filter(text__icontains=query)

    return render_to_response("blog/post_list.html", {"post_list": post_list, "query": query})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comment = Comment.objects.filter(comment_post_id=pk)
    return render_to_response("blog/post_detail.html", {"post": post, "comment": comment})


def test(request):
    form = OrderForm(request.POST or None)
    def name():
        if request.method == "POST":
            if form.is_valid():
                return request.POST.get('name')
    return render(request, "blog/test.html", {"form": form, "name": name})




