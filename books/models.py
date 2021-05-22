from django.db import models
from django.db.models.fields import AutoField, CharField

class BooksModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    price = models.FloatField()
    img = models.FileField()

    
class Meta:
    db_table = 'booksmodel'
