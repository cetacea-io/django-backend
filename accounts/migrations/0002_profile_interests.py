# Generated by Django 2.1 on 2019-02-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20190103_0846'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='users_interested', to='category.Category'),
        ),
    ]
