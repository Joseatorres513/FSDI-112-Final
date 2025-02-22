from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from .models import Post
from django.urls import reverse_lazy


class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body",
        "author",
    ]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = [
        "title", "subtitle", "body",
        "author",
    ]

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "post_list"