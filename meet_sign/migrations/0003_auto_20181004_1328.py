# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet_sign', '0002_auto_20180413_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='bank_account',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u94f6\u884c\u8d26\u6237', blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='company_address',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u4f01\u4e1a\u5730\u5740', blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='taxpayer_number',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u7eb3\u7a0e\u4eba\u8bc6\u522b\u53f7', blank=True),
        ),
    ]
