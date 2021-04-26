# Generated by Django 3.2 on 2021-04-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0019_alter_drinktag_tagname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodtag',
            name='tags',
        ),
        migrations.AddField(
            model_name='foodtag',
            name='tagname',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drink',
            name='group',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='drink',
            name='lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='drink',
            name='lon',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='drink',
            name='photo_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drink',
            name='tags',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='food',
            name='group',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='food',
            name='lon',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='food',
            name='photo_url',
            field=models.CharField(default='l', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='tags',
            field=models.CharField(max_length=20),
        ),
    ]