# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet_sign', '0003_cost_meet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_payment',
        ),
    ]
