# Generated by Django 2.1 on 2019-04-09 16:48

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('courses', '0005_auto_20190409_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseType',
            new_name='CourseClassification',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_type',
            new_name='classification',
        ),
    ]
