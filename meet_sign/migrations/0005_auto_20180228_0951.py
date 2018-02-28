# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet_sign', '0004_remove_order_is_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='logo',
            field=models.CharField(default=b'', max_length=500, null=True, verbose_name='\u5934\u50cf', blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u59d3\u540d', blank=True),
        ),
    ]
