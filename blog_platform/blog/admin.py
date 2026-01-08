from django.contrib import admin

from .models import Post, PostTestimonial


admin.site.register(PostTestimonial)

class PostTestimonialAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post", "checked")  # показываем поле checked в списке
    list_editable = ("checked",)  # можно ставить галочку прямо в списке

admin.site.register(Post)