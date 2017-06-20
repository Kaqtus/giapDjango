from django.shortcuts import render
from django.utils import timezone
from .models import Post


def produkty(request):
    return render(request, 'administracja_publiczna/produkty.html', {})


# PRODUKTY

def turysta(request):
    h1 = "Turysta"
    h2 = "Aplikacja GIS do zarządzania obiektami turystycznymi"
    return render(request, 'administracja_publiczna/turysta.html', {'h1': h1, 'h2': h2})


def ekolog(request):
    h1 = "Ekolog"
    h2 = ""
    return render(request, 'administracja_publiczna/ekolog.html', {'h1': h1})


def adresat(request):
    h1 = "Adresat"
    h2 = ""
    return render(request, 'administracja_publiczna/adresat.html', {'h1': h1})

# PRODUKTY KONIEC

def kontakt(request):
    return render(request, 'administracja_publiczna/kontakt.html', {})


def akty_prawne(request):
    return render(request, 'administracja_publiczna/akty_prawne.html', {})


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'administracja_publiczna/index.html', {'posts': posts})


def aktualnosci(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'administracja_publiczna/aktualnosci.html', {'posts': posts})


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'administracja_publiczna/post.html', {'post': post})
