# Generated by Django 5.0.2 on 2024-11-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_users_long_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
    ]