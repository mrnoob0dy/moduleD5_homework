from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import NewsForm
from .models import BaseRegisterForm



class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10


class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'filter'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
    

class PostsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('newapp.add_post',)
    template_name = 'posts_create.html'
    form_class = NewsForm


class PostsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('newapp.change_post',)
    template_name = 'posts_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    


class PostsDeleteView(DeleteView):
    template_name = 'posts_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'



class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')