from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post, Status
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    
)

#from django.urls import reverse this creates lookup url function


class PostListView(ListView):    #scan operation
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub_status = Status.objects.get(name="published")
        context["post_list"] = (
            Post.objects
            .filter(status=pub_status)
            .order_by("created_on").reverse()
        )
        return context

class DraftPostListView(LoginRequiredMixin, ListView): 
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["post_list"] = (
            Post.objects
            .filter(status=draft_status)
            .filter(author=self.request.user) 
            .order_by("created_on").reverse()
            )
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        arch_status = Status.objects.get(name="archived")
        context["post_list"] = (
            Post.objects
            .filter(status=arch_status)
            .order_by("created_on").reverse()
        )
        return context



class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):  #read single
    template_name = "posts/detail.html"
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    
    
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
        
class PostUpdateToDraftView(UpdateView):
    template_name = "posts/update_status.html"
    models = Post
    fields = ["status"]
