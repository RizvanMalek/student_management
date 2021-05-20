from django.db import models

# Create your models here.
class AdminModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=6)
    is_active = models.IntegerField(max_length=1)

class Meta:
    db_table = 'AdminModel'
