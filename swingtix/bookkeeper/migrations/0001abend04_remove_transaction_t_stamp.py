# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0001abend03_transaction_copy_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='t_stamp',
        ),
    ]
