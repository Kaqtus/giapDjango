from django.shortcuts import render

def index(request):
    return render(request, 'skanowanie_laserowe/index.html', {})