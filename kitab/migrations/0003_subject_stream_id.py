# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0002_auto_20150617_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='stream_id',
            field=models.ForeignKey(to='kitab.stream', null=True),
            preserve_default=True,
        ),
    ]
