# Generated by Django 4.2 on 2024-10-27 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0005_remove_conferences_the_start_date_must_be_greater_than_today_or_equal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferences',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 27, 17, 31, 11, 105265, tzinfo=datetime.timezone.utc)),
        ),
    ]
