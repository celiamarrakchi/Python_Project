# Generated by Django 4.2 on 2024-10-27 17:21

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, validators=[categories.models.validate_letters_only]),
        ),
    ]
