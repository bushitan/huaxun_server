# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0009_auto_20181004_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='share_image_url',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5206\u4eab\u56fe\u7247', blank=True),
        ),
        migrations.AddField(
            model_name='meet',
            name='share_path',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u5206\u4eab\u8def\u5f84', blank=True),
        ),
        migrations.AddField(
            model_name='meet',
            name='share_title',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u5206\u4eab\u6807\u9898', blank=True),
        ),
        migrations.AlterField(
            model_name='meet',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='\u7eac\u5ea6'),
        ),
        migrations.AlterField(
            model_name='meet',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='\u7ecf\u5ea6'),
        ),
    ]
