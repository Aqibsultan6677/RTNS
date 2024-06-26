# Generated by Django 4.2.7 on 2024-04-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_patronimage_patron_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='patrons/')),
            ],
        ),
        migrations.DeleteModel(
            name='PatronImage',
        ),
    ]
