# Generated by Django 3.2 on 2021-05-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_india'),
    ]

    operations = [
        migrations.AddField(
            model_name='india',
            name='age',
            field=models.IntegerField(default=-1, max_length=1),
            preserve_default=False,
        ),
    ]
