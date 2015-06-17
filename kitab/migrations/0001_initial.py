# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200)),
                ('book_isbn', models.IntegerField(max_length=13)),
                ('book_edition', models.CharField(max_length=50)),
                ('book_pdf_link', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('course_desc', models.TextField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='course_subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stream_name', models.CharField(max_length=50)),
                ('stream_desc', models.TextField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subject_book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_id', models.ForeignKey(to='kitab.book')),
                ('subject_id', models.ForeignKey(to='kitab.subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course_subject',
            name='stream_id',
            field=models.ForeignKey(to='kitab.stream'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course_subject',
            name='subject_id',
            field=models.ForeignKey(to='kitab.subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='stream_id',
            field=models.ForeignKey(to='kitab.stream'),
            preserve_default=True,
        ),
    ]
