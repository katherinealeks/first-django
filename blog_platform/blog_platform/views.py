from django.http import HttpResponse
from django.shortcuts import render


MENU = {"Главная": "/", "О блоге": "/about", "Пост": "/post"}


def main_page(request):
    title = "Путешествия без границ"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)


def about(request):
    title = "Блог о путешествиях"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)


def post(request):
    title = "Прогулка по Кёльну"
    data = {"menu": MENU, "title": title}
    return render(request, "./post.html", context=data)