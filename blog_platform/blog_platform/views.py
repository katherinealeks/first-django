from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, PostTestimonial

MENU = {"Главная": "/", "О блоге": "/about", "Пост": "/post", "Отзывы": "/add_testimonial"}


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

def add_testimonial_page(request):
    posts = Post.objects.values("id", "name")
    testimonials = PostTestimonial.objects.filter(checked=True).order_by('-id')
    title = "Добавить отзыв"
    data = {"menu": MENU, "title": title, "posts": posts, "testimonials": testimonials,}
    return render(request, "./add_testimonial.html", context=data)

def thanks_page(request):
    user_name = request.POST['user_name']
    testimonial = request.POST['testimonial']
    post = Post.objects.get(pk=request.POST['post'])
    PostTestimonial.objects.create(user_name = user_name, testimonial=testimonial, post=post)
    title = "Страница благодарностей"
    data = {"menu": MENU, "title": title, "user_name": user_name}
    return render(request, "./thanks_page.html", context=data)