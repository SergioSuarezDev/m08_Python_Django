from django.shortcuts import render

# Create your views here.


import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from posts.forms import PostForm
from posts.models import Post, Category


class LatestPostsView(View):

    def get(self, request):
        posts = Post.objects.all().filter(publication_date__lte=datetime.datetime.now()).order_by('-modification_date').select_related('owner')
        context = {'posts': posts[:6]}
        html = render(request, 'latest.html', context)
        return HttpResponse(html)


class PostDetailView(View):
    def get(self, request, username, pk):
        post = get_object_or_404(Post.objects.select_related('owner'), pk=pk )
        context = {'post': post}
        html = render(request, 'detail.html', context)
        return HttpResponse(html)


class NewPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'new.html', context)

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post successfully created')
            form = PostForm()

        context = {'form': form}
        return render(request, 'new.html', context)


class PostList(object):

    def get_queryset(self):
        queryset = Post.objects.select_related('owner').order_by('-publication_date')
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(publication_date__lte=datetime.datetime.now())
        elif not self.request.user.is_superuser:
            queryset = queryset.filter(Q(publication_date__lte=datetime.datetime.now()) | Q(owner=self.request.user))
        return queryset


