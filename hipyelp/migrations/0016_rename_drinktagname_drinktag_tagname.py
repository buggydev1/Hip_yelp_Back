# Generated by Django 3.2 on 2021-04-25 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hipyelp', '0015_alter_drinktag_drinktagname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinktag',
            old_name='drinktagName',
            new_name='tagName',
        ),
    ]