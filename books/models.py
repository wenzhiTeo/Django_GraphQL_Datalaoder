from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    text = models.TextField()

