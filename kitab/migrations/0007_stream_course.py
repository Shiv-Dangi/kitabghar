# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0006_auto_20150716_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='stream_course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_id', models.ForeignKey(to='kitab.course')),
                ('stream_id', models.ForeignKey(to='kitab.stream')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
