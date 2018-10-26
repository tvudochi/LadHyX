# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='debut_mail',
            field=models.CharField(null=True, blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personnel',
            name='fin_mail',
            field=models.CharField(null=True, blank=True, max_length=500),
            preserve_default=True,
        ),
    ]
