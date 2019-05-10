from django.db import models
from manager.constants import BookState

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    publication_year = models.IntegerField()
    state = models.IntegerField(choices=BookState.CHOISES)

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, null=True, blank=True)

    book = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.name





# Defining a model/database table is as simple as creating a new class
# The class attributes are the columns of the table
