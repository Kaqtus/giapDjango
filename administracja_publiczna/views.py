from django.shortcuts import render


def index(request):
    h1 = "Administracja publiczna"
    h2 = ""
    return render(request, 'administracja_publiczna/index.html', {"h1": h1, "h2": h2})


def akty_prawne(request):
    return render(request, 'administracja_publiczna/akty_prawne.html', {})


def partynerzy(request):
    h1 = "Nasi partnerzy"
    h2 = ""
    return render(request, 'administracja_publiczna/partnerzy.html', {"h1": h1, "h2": h2})


# PRODUKTY


def produkty(request):
    return render(request, 'administracja_publiczna/produkty.html', {})


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