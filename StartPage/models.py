from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=25)
    about = models.TextField(max_length=2500)
    img = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field'
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Verse(models.Model):
    name = models.CharField(max_length=25)
    text = models.TextField(max_length=2500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}-{self.author}'
