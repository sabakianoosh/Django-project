# Generated by Django 3.2.9 on 2021-11-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0005_rename_book_id_book_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book_id',
        ),
    ]