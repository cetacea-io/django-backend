# Generated by Django 2.1 on 2019-04-11 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190409_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_and_time',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.DateAndTime'),
        ),
    ]
