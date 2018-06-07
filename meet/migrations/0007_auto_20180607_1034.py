# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0006_auto_20180607_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='introduction',
            field=models.TextField(default=b'', null=True, verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True),
        ),
    ]
