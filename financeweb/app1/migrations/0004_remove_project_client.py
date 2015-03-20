# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
    ]
