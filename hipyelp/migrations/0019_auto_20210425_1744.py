# Generated by Django 3.2 on 2021-04-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0018_auto_20210425_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ftag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='drinks', to='hipyelp.Ftag'),
        ),
        migrations.AddField(
            model_name='food',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='foods', to='hipyelp.Ftag'),
        ),
    ]