# Generated by Django 3.2.16 on 2023-02-19 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa_app', '0009_auto_20230219_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='file_comments',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spa_app.comments'),
        ),
        migrations.AddField(
            model_name='comments',
            name='photo_comments',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
