# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-11-18 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_message_edito'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='position',
            field=models.CharField(choices=[('right', 'Droite'), ('left', 'Gauche'), ('top', 'Haut')], default='top', max_length=6, verbose_name='position de l image'),
        ),
    ]
