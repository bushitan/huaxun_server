# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0001_initial'),
        ('meet_sign', '0002_auto_20180222_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='meet',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True),
        ),
    ]
