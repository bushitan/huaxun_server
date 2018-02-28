# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0002_auto_20180227_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelibrary',
            name='style',
            field=models.IntegerField(default=2, verbose_name='\u6587\u7ae0\u7c7b\u522b', choices=[(1, b'\xe6\x99\xae\xe9\x80\x9a'), (2, b'\xe7\xba\xaf\xe6\x96\x87\xe5\xad\x97'), (3, b'\xe9\x9f\xb3\xe9\xa2\x91'), (4, b'\xe8\xa7\x86\xe9\xa2\x91')]),
        ),
    ]
