# Generated by Django 5.0.1 on 2024-01-31 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_alter_livestream_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 5, 35, 5, 54322, tzinfo=datetime.timezone.utc)),
        ),
    ]
