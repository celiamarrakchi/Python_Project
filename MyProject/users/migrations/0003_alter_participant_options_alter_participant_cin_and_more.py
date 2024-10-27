# Generated by Django 4.2 on 2024-10-27 17:21

import django.core.validators
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_participant_reservations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'verbose_name_plural': 'Participant'},
        ),
        migrations.AlterField(
            model_name='participant',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='this field must containt exactly 8 numbers', regex='^\\d{8}$')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[users.models.email_validator]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]