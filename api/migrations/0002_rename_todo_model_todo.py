# Generated by Django 4.0.1 on 2022-02-16 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo_model',
            new_name='Todo',
        ),
    ]
