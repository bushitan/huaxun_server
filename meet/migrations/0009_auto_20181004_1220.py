# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0008_meet_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='hotel',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u9152\u5e97\u540d\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='meet',
            name='phone',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u7535\u8bdd', blank=True),
        ),
    ]
