# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0004_bookrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_no', models.IntegerField(max_length=13)),
                ('message', models.TextField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
