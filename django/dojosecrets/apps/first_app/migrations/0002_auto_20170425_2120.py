# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_on', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to='first_app.Users')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='first_app.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcontent', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.BigIntegerField()),
                ('users_posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whoposted', to='first_app.Users')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
