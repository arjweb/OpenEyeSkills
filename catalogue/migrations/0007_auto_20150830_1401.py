# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_catalogueitem_discovered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogueitem',
            name='description',
            field=models.TextField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='catalogueitem',
            name='how_apply',
            field=models.TextField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='catalogueitem',
            name='what_learn',
            field=models.TextField(max_length=2000, blank=True),
        ),
    ]
