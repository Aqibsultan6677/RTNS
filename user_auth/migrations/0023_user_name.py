# Generated by Django 4.2.7 on 2024-03-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0022_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='hamza', max_length=100),
        ),
    ]