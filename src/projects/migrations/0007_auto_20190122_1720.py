# Generated by Django 2.1 on 2019-01-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_position_compensation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='form',
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]