# Generated by Django 5.0.3 on 2024-04-18 06:12

import django.db.models.deletion
import partials.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partials', '0009_alter_departmentlogo_logo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitefooter',
            name='sponsor_logo',
        ),
        migrations.CreateModel(
            name='SponsorLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/footer', validators=[partials.models.max_sponsor_logos])),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_logos', to='partials.websitefooter')),
            ],
        ),
    ]
