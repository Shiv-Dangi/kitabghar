# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_subject',
            name='stream_id',
        ),
        migrations.AddField(
            model_name='course_subject',
            name='course_id',
            field=models.ForeignKey(to='kitab.course', null=True),
            preserve_default=True,
        ),
    ]
