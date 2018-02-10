# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TBLSessions', '0015_auto_20180203_2350'),
        ('questions', '0029_auto_20180209_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisesubmission',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_submissions', to='TBLSessions.TBLSession', verbose_name='TBL sessions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gratsubmission',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grat_submissions', to='TBLSessions.TBLSession', verbose_name='TBL sessions'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iratsubmission',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='irat_submissions', to='TBLSessions.TBLSession', verbose_name='TBL sessions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('Intermediary', 'Intermediary'), ('Basic', 'Basic'), ('Advanced', 'Advanced')], default='basic', help_text='Difficulty level', max_length=15, verbose_name='Level'),
        ),
    ]
