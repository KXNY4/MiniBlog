from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormMixin

from Posts.models import Posts
from Posts.utils import PostsDataMixin
from Posts.forms import PostsCreateForm

from Comments.forms import CommentForm


class PostsListView(PostsDataMixin, ListView):
    model = Posts
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    title = 'Посты'
    ordering = ['-created_at']

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)
    

class PostsCreateView(LoginRequiredMixin, PostsDataMixin, CreateView):
    model = Posts
    form_class = PostsCreateForm
    template_name = 'posts/create.html'
    extra_context = {
        'title': 'Создание поста'
    }
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(PostsDataMixin, FormMixin, DetailView):
    model = Posts
    template_name = 'posts/post.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    form_class = CommentForm
    extra_context = {
        'title': 'Пост'
    }


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return super().form_valid(form)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _(str(kwargs.get('title', None)))
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['user_has_liked'] = self.object.liked_posts.filter(user=self.request.user).exists()
        return self.get_mixin_context(context)
    
    def get_success_url(self):
        return self.object.get_absolute_url()


class PostsUserView(LoginRequiredMixin, PostsDataMixin, ListView):
    model = Posts
    template_name = 'posts/posts_user.html'
    context_object_name = 'posts'
    title = 'Мои посты'
    ordering = ['-created_at']

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class PostDeleteView(LoginRequiredMixin, PostsDataMixin, DeleteView):
    model = Posts
    title = 'Удалить?'
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:home')
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)