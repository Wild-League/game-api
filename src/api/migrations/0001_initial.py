# Generated by Django 5.0.2 on 2024-11-18 15:35

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('display_name', models.CharField(max_length=85)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('domain', models.CharField(max_length=60)),
                ('url', models.CharField(max_length=255)),
                ('long_url', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.TextField()),
                ('inbox_url', models.CharField(max_length=255)),
                ('outbox_url', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('edited_at', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(null=True)),
                ('level', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('agreement', models.BooleanField(blank=True, null=True)),
                ('public_key', models.CharField(blank=True, null=True)),
                ('private_key', models.CharField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(blank=True, null=True)),
                ('is_staff', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
                ('life', models.IntegerField(blank=True, null=True)),
                ('speed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('attack_range', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cooldown', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('damage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('frame_width', models.IntegerField(blank=True, null=True)),
                ('frame_height', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('img_card', models.CharField(blank=True, max_length=255, null=True)),
                ('img_preview', models.CharField(blank=True, max_length=255, null=True)),
                ('img_attack', models.CharField(blank=True, max_length=255, null=True)),
                ('img_death', models.CharField(blank=True, max_length=255, null=True)),
                ('img_walk', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rules',
            },
        ),
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'waitlist',
            },
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'deck',
            },
        ),
        migrations.CreateModel(
            name='DeckCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.deck')),
            ],
            options={
                'db_table': 'deck_card',
            },
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(through='api.DeckCard', to='api.card'),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField()),
                ('edited_at', models.DateField(blank=True, null=True)),
                ('content', models.CharField(max_length=255)),
                ('in_reply_to_post_id', models.ForeignKey(blank=True, db_column='in_reply_to_post_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.posts')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='UsersRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_type', models.CharField(choices=[('Block', 'Block'), ('Friend', 'Friend'), ('FriendRequest', 'Friendrequest'), ('Rejected', 'Rejected')], max_length=25)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('activity_id', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id_related', models.ForeignKey(db_column='user_id_related', on_delete=django.db.models.deletion.RESTRICT, related_name='user_id_related', to=settings.AUTH_USER_MODEL)),
                ('user_id_requester', models.ForeignKey(db_column='user_id_requester', on_delete=django.db.models.deletion.RESTRICT, related_name='user_id_requester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_relationship',
            },
        ),
    ]
