# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0013_auto_20180611_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecertificate',
            name='certificate_type',
            field=models.CharField(choices=[('honor', 'honor'), ('professional', 'professional'), ('verified', 'verified'), ('no-id-professional', 'no-id-professional')], max_length=255),
        ),
    ]
