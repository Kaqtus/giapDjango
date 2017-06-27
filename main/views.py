from django.shortcuts import render
from django.utils import timezone
from .models import Post


def sitemap(request):
    return render(request, 'main/sitemap.html', {})


def kontakt(request):
    return render(request, 'main/kontakt.html', {})


def aktualnosci(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'main/aktualnosci.html', {'posts': posts})


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/post.html', {'post': post})


def index(request):
    h1 = "GIAP"
    h2 = "Nagłówek do wymyślenia"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'main/index.html', {'posts': posts, "h1": h1, "h2": h2})
