# Generated by Django 5.0.2 on 2024-06-06 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_card_img_attack_card_img_card_card_img_death_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='height',
            new_name='frame_height',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='width',
            new_name='frame_width',
        ),
    ]