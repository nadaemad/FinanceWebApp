# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ename', models.CharField(max_length=50)),
                ('eamount', models.IntegerField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gprofit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pamount', models.IntegerField(max_length=20)),
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
                ('exp', models.ManyToManyField(to='app1.Expense')),
                ('prof', models.ForeignKey(to='app1.Gprofit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.CharField(max_length=120, unique=True, null=True)),
                ('user_name', models.CharField(max_length=120, unique=True, null=True)),
                ('first_name', models.CharField(max_length=120)),
                ('Last_name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('confirm_password', models.CharField(max_length=120)),
                ('company_name', models.CharField(unique=True, max_length=200)),
                ('company_date_of_origin', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
