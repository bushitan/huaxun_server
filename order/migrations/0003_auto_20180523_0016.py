# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20180523_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ['-create_time'], 'verbose_name': '2.2 \u4f18\u60e0\u5238', 'verbose_name_plural': '2.2 \u4f18\u60e0\u5238'},
        ),
        migrations.AlterModelOptions(
            name='discounttemplate',
            options={'ordering': ['-create_time'], 'verbose_name': '2.3 \u4f18\u60e0\u5238\u6a21\u677f', 'verbose_name_plural': '2.3 \u4f18\u60e0\u5238\u6a21\u677f'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-create_time'], 'verbose_name': '2.1 \u8ba2\u5355', 'verbose_name_plural': '2.1 \u8ba2\u5355'},
        ),
    ]
