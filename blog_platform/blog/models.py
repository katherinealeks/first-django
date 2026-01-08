from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=200, blank=False)
    topic =models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return f'{self.topic} | {self.name}'


class PostTestimonial(models.Model):
    user_name = models.CharField(max_length=200, blank=False)
    testimonial = models.CharField(max_length=600, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name} | {self.testimonial}'