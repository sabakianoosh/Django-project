# Generated by Django 3.2.9 on 2021-11-12 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0007_alter_book_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='name',
        ),
    ]
