# Generated by Django 4.1.6 on 2023-12-26 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NationalSpeakers',
            new_name='InterNationalSpeaker',
        ),
        migrations.RenameModel(
            old_name='InterNationalSpeakers',
            new_name='NationalSpeaker',
        ),
    ]
