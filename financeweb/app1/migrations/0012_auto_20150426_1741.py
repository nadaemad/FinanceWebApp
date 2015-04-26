# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20150426_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.RemoveField(
            model_name='project',
            name='exp',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.RemoveField(
            model_name='project',
            name='prof',
        ),
        migrations.DeleteModel(
            name='Gprofit',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
