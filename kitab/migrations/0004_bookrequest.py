# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0003_subject_stream_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookrequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('user_emailid', models.EmailField(max_length=254)),
                ('book_name', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200)),
                ('book_edition', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
