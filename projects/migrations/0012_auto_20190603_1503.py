# Generated by Django 2.1 on 2019-06-03 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('projects', '0011_auto_20190502_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.AddField(
            model_name='project',
            name='author_content_type',
            field=models.ForeignKey(default=1, limit_choices_to=models.Q(models.Q(('app_label', 'users'), ('model', 'a')), models.Q(('app_label', 'organizations'), ('model', 'Organization')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='author_object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
