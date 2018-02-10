# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 01:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0028_auto_20180209_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='gratsubmission',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grat_submissions', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Intermediary', 'Intermediary'), ('Advanced', 'Advanced')], default='basic', help_text='Difficulty level', max_length=15, verbose_name='Level'),
        ),
    ]
