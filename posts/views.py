from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post 

#from django.urls import reverse this creates lookup url function


class PostListView(ListView):    #scan operation
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):  #read single
    template_name = "posts/detail.html"
    model = Post

    fields = ["id"]
    
class PostUpdateView(UpdateView):  #read single
    template_name = "posts/update.html"
    model = Post    
    fields = ["title", "subtitle", "body", "status"]


class PostCreateView(CreateView):   #create new post
    template_name = "posts/new.html"
    model = Post    
    fields = ["title", "author", "subtitle", "body", "status"]


class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

