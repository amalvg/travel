# Generated by Django 3.1.3 on 2020-12-11 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='news',
            new_name='blog',
        ),
    ]