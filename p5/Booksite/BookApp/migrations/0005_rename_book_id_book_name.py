# Generated by Django 3.2.9 on 2021-11-12 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0004_auto_20211111_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='name',
        ),
    ]