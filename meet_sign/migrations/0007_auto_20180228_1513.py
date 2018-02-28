# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet_sign', '0006_attendee_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_alive',
            field=models.IntegerField(default=1, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b'), (3, '\u65e0\u610f\u4e49')]),
        ),
        migrations.AlterField(
            model_name='sign',
            name='is_alive',
            field=models.BooleanField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b'), (3, '\u65e0\u610f\u4e49')]),
        ),
    ]
