from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name= 'home.html'
    paginate_by = 4

class BlogDetailVIew(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'postdetail'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class BlogCreateView(CreateView):
    model = Post
    template_name = "create.html"
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "edit.html"
    fields = ['title','body',]