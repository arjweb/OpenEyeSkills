# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_topicarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogueItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('link', models.CharField(max_length=255)),
                ('discovered_by', models.CharField(max_length=50)),
                ('what_learn', models.CharField(blank=True, max_length=2000)),
                ('how_apply', models.CharField(blank=True, max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('job', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('level_desc', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='topicarea',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='catalogueitem',
            name='level',
            field=models.ForeignKey(to='catalogue.Level'),
        ),
        migrations.AddField(
            model_name='catalogueitem',
            name='relevant_to',
            field=models.ManyToManyField(to='catalogue.JobType'),
        ),
        migrations.AddField(
            model_name='catalogueitem',
            name='topic_area',
            field=models.ForeignKey(to='catalogue.TopicArea'),
        ),
    ]
