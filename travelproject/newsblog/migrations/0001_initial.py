# Generated by Django 3.1.3 on 2020-12-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='news')),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
