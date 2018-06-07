# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0005_auto_20180413_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'ordering': ['-create_time'], 'verbose_name': '6.1.1 \u76ee\u5f55 -- \u65e5\u7a0b', 'verbose_name_plural': '6.1.1 \u76ee\u5f55 -- \u65e5\u7a0b'},
        ),
        migrations.AlterModelOptions(
            name='guest',
            options={'ordering': ['-create_time'], 'verbose_name': '6.1.2 \u76ee\u5f55 -- \u5609\u5bbe', 'verbose_name_plural': '6.1.2 \u76ee\u5f55 -- \u5609\u5bbe'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-create_time'], 'verbose_name': '6.1.3 \u76ee\u5f55 -- \u65b0\u95fb', 'verbose_name_plural': '6.1.3 \u76ee\u5f55 -- \u65b0\u95fb'},
        ),
        migrations.AlterModelOptions(
            name='spot',
            options={'ordering': ['-create_time'], 'verbose_name': '6.1.4 \u76ee\u5f55 -- \u666f\u70b9', 'verbose_name_plural': '6.1.4 \u76ee\u5f55 -- \u666f\u70b9'},
        ),
        migrations.AlterModelOptions(
            name='swiper',
            options={'ordering': ['-create_time'], 'verbose_name': '6.2 \u8f6e\u64ad\u56fe', 'verbose_name_plural': '6.2 \u8f6e\u64ad\u56fe'},
        ),
        migrations.AlterField(
            model_name='guest',
            name='introduction',
            field=models.CharField(default=b'', max_length=2000, null=True, verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True),
        ),
    ]
