# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20150404_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='companyname',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
