# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-18 11:22
# Generated by Django 1.9.7 on 2016-11-14 14:51

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobili', '0028_auto_20161111_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2016-11-18 08:22'),
            preserve_default=False,
        ),
    ]
