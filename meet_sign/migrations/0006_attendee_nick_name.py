# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet_sign', '0005_auto_20180228_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='nick_name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5fae\u4fe1\u6635\u79f0', blank=True),
        ),
    ]
