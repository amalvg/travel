# Generated by Django 3.1.3 on 2020-12-05 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_auto_20201204_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='img',
            new_name='image',
        ),
    ]