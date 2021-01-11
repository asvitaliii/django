from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=25)
    about = models.TextField(max_length=2500)
    img = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Verse(models.Model):
    name = models.CharField(max_length=25)
    text = models.TextField(max_length=2500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.author}'
