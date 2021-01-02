from django.db import models


class Verse(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    text = models.TextField(max_length=2500)