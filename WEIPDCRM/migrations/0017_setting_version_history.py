# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0016_auto_20170402_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='version_history',
            field=models.BooleanField(default=False, help_text='Enable version history module', verbose_name='Version History'),
        ),
    ]
