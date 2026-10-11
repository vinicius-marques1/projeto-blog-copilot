from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def posts(request):
    return render(request, "posts.html")


def sobre(request):
    return render(request, "sobre.html")
