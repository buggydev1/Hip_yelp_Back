# Generated by Django 3.2 on 2021-04-25 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0013_alter_drinktag_tagname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinktag',
            old_name='tagName',
            new_name='drinktagName',
        ),
    ]
