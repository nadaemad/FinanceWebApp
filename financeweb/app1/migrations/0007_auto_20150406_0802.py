# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20150404_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='project',
            name='prof',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
