# Generated by Django 3.1.3 on 2020-12-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='news')),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
