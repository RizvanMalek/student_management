# Generated by Django 3.2 on 2021-05-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=6)),
                ('is_active', models.IntegerField(max_length=1)),
            ],
        ),
    ]
