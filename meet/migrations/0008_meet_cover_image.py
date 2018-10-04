# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0007_auto_20180607_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='cover_image',
            field=models.ForeignKey(verbose_name='\u5c01\u9762\u56fe\u7247', blank=True, to='meet.ImageLibrary', null=True),
        ),
    ]
