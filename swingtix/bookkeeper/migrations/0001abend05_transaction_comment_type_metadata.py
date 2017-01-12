# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0001abend04_remove_transaction_t_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='comment',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='metadata',
            field=models.TextField(default='{}'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
