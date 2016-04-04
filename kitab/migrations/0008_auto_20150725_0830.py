# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0007_stream_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='stream_id',
        ),
        migrations.AddField(
            model_name='subject',
            name='course_id',
            field=models.ForeignKey(to='kitab.course', null=True),
            preserve_default=True,
        ),
    ]
