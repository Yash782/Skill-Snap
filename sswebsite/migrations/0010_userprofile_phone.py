# Generated by Django 5.0.1 on 2024-01-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sswebsite', '0009_remove_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
