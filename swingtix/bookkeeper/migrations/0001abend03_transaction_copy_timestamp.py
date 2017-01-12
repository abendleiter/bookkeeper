# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


from django.db import migrations, models


def copy_timestamps(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Transaction = apps.get_model("bookkeeper", "Transaction")
    Transaction.objects.update(timestamp=models.F('t_stamp'))


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0001abend02_transaction_timestamp'),
    ]

    operations = [
        migrations.RunPython(copy_timestamps, reverse_code=migrations.RunPython.noop)
    ]
