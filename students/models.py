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
