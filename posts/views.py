from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post 
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    
)

#from django.urls import reverse this creates lookup url function


class PostListView(ListView):    #scan operation
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):  #read single
    template_name = "posts/detail.html"
    model = Post

    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  #read single
    template_name = "posts/update.html"
    model = Post    
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):   #create new post
    template_name = "posts/new.html"
    model = Post    
    fields = ["title", "author", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
        

