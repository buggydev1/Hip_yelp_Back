# Generated by Django 3.2 on 2021-04-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0009_auto_20210425_0219'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HotSpotTag',
            new_name='FoodTag',
        ),
        migrations.CreateModel(
            name='DrinkTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinkName', models.ManyToManyField(related_name='tags', related_query_name='tag', to='hipyelp.Drink')),
            ],
        ),
    ]