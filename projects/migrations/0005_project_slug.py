# Generated by Django 5.0.3 on 2024-04-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=12, max_length=150),
            preserve_default=False,
        ),
    ]