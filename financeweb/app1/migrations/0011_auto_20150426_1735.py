# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20150408_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='eamount',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gprofit',
            name='pamount',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
