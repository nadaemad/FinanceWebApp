# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0014_auto_20150427_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_created', models.DateTimeField(null=True, blank=True)),
                ('date_to_remind', models.DateField(null=True, blank=True)),
                ('time_to_remind', models.TimeField(default=datetime.time(0, 0), null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
