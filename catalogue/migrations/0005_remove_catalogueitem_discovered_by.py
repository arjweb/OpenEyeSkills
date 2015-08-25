# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20150825_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogueitem',
            name='discovered_by',
        ),
    ]
