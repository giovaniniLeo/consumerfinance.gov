# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-12 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0218_auto_20200511_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportsubsection',
            old_name='header',
            new_name='subheader',
        ),
    ]
