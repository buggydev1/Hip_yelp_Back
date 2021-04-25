# Generated by Django 3.2 on 2021-04-25 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0016_rename_drinktagname_drinktag_tagname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinktag',
            name='drinkName',
        ),
        migrations.RemoveField(
            model_name='drinktag',
            name='tagName',
        ),
        migrations.RemoveField(
            model_name='foodtag',
            name='foodName',
        ),
        migrations.RemoveField(
            model_name='foodtag',
            name='tagName',
        ),
        migrations.AddField(
            model_name='drinktag',
            name='tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='hipyelp.drink'),
        ),
        migrations.AddField(
            model_name='foodtag',
            name='tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='hipyelp.food'),
        ),
    ]
