# Generated by Django 3.2 on 2021-05-22 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_india_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='india',
            name='name',
        ),
    ]
