# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_expense_gprofit_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revenue_name', models.CharField(max_length=50)),
                ('revenue_amount', models.IntegerField()),
                ('revenue_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='revenues',
            field=models.ManyToManyField(to='app1.Revenue'),
            preserve_default=True,
        ),
    ]
