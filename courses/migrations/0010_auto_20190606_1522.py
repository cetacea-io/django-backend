# Generated by Django 2.1 on 2019-06-06 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20190606_1522'),
        ('events', '0004_auto_20190606_1522'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DateAndTime',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
