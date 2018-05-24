from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    front_cover = models.ImageField()

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
