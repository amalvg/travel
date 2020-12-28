# Generated by Django 3.1.3 on 2020-12-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_auto_20201205_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100)),
                ('img1', models.ImageField(upload_to='spcl')),
                ('desc1', models.TextField()),
                ('price1', models.IntegerField(default=0)),
            ],
        ),
    ]
