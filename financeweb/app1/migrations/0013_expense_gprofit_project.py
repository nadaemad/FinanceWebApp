# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20150426_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ename', models.CharField(max_length=50)),
                ('eamount', models.IntegerField()),
                ('expense_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gprofit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pamount', models.IntegerField()),
                ('profit_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
