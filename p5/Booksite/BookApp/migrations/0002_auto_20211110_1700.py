# Generated by Django 3.2.8 on 2021-11-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='summery',
            field=models.TextField(max_length=256, null=True),
        ),
    ]
