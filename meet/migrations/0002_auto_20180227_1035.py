# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelibrary',
            name='style',
            field=models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u7c7b\u522b', choices=[(0, '\u4e00\u822c'), (1, '\u7f6e\u9876')]),
        ),
    ]
