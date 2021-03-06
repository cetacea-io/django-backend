# Generated by Django 2.1 on 2019-06-06 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190606_1522'),
        ('category', '0002_auto_20190103_0846'),
        ('projects', '0012_auto_20190603_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='project',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='projects_project_related', to='category.Category'),
        ),
        migrations.AddField(
            model_name='project',
            name='date_and_time',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.DateAndTime'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='projects_project_related', to='category.Tag'),
        ),
        migrations.AlterField(
            model_name='project',
            name='author_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'users'), ('model', 'user')), models.Q(('app_label', 'organizations'), ('model', 'organization')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
