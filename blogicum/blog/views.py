from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('category').filter(
        category__is_published=True,
        is_published=True,
        pub_date__lt=timezone.now()
    ).order_by('-pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'

    post = get_object_or_404(Post.objects.filter(
        id=id,
        pub_date__lt=timezone.now(),
        is_published=True,
        category__is_published=True
    ).select_related('author', 'category'))

    context = {'post': post}
    return render(request, template, context)


def category_post(request, category_slug) -> str:
    template = 'blog/category.html'

    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug,
    )

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lt=timezone.now()
    ).select_related('author', 'category')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
