# Generated by Django 3.1.7 on 2021-04-14 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200724_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttag',
            name='post',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1),
        ),
        migrations.DeleteModel(
            name='PostStatus',
        ),
        migrations.DeleteModel(
            name='PostTag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
