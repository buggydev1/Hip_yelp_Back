# Generated by Django 3.2 on 2021-04-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0006_auto_20210422_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='lat',
            field=models.CharField(default='lat', max_length=20),
        ),
        migrations.AddField(
            model_name='drink',
            name='lon',
            field=models.CharField(default='lon', max_length=20),
        ),
        migrations.AddField(
            model_name='food',
            name='lat',
            field=models.CharField(default='lat', max_length=20),
        ),
        migrations.AddField(
            model_name='food',
            name='lon',
            field=models.CharField(default='lon', max_length=20),
        ),
    ]
