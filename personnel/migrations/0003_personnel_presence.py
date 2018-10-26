# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_auto_20160219_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='presence',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
