from django.db import models
from django.db.models.fields import AutoField, CharField, IntegerField

# Create your models here.
class StudentsModel(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=25)
    email = CharField(max_length=25)
    password = CharField(max_length=6)
    is_active = IntegerField(max_length=1)

class Meta:
    db_table = 'StudentModel'

class India(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(max_length=1)



