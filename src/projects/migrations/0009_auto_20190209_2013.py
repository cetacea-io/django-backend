# Generated by Django 2.1 on 2019-02-09 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_position_applicants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='author',
        ),
    ]
