# Generated by Django 4.2.16 on 2024-11-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
