# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0005_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_no',
            field=models.BigIntegerField(max_length=13),
            preserve_default=True,
        ),
    ]
