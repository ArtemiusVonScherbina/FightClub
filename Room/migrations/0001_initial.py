# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game_type', models.CharField(choices=[('SP', 'Simpleplay'), ('MP', 'Multiplay')], max_length=3)),
                ('date_begin', models.DateField(auto_now=True)),
                ('date_end', models.DateField(blank=True)),
            ],
        ),
    ]
