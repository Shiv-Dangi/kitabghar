# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitab', '0009_auto_20150806_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_isbn',
            field=models.IntegerField(),
        ),
    ]
