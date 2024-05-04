# Generated by Django 4.2.7 on 2024-03-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_rename_nationalspeakers_internationalspeaker_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='speakers/national_speakers/')),
                ('designation', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('spekaer_type', models.CharField(blank=True, choices=[('national', 'National'), ('international', 'International')], max_length=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='InterNationalSpeaker',
        ),
        migrations.DeleteModel(
            name='NationalSpeaker',
        ),
    ]
