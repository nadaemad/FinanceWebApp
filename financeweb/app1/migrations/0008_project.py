# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20150406_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=30)),
                ('client', models.ForeignKey(to='app1.UserProfile')),
                ('exp', models.ManyToManyField(to='app1.Expense')),
                ('prof', models.ForeignKey(to='app1.Gprofit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
