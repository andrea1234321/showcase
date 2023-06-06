# Generated by Django 4.2.2 on 2023-06-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_show_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='photo',
        ),
        migrations.AddField(
            model_name='show',
            name='url',
            field=models.URLField(default=1, verbose_name='URL link:'),
            preserve_default=False,
        ),
    ]