# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '1.6 \u7528\u6237_\u4f01\u4e1a\u4fe1\u606f', 'verbose_name_plural': '1.6 \u7528\u6237_\u4f01\u4e1a\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='imagemap',
            options={'verbose_name': '1.4   \u56fe\u5e93', 'verbose_name_plural': '1.4   \u56fe\u5e93'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['-value'], 'verbose_name': '1.2 \u4f1a\u5458\u89d2\u8272', 'verbose_name_plural': '1.2 \u4f1a\u5458\u89d2\u8272', 'permissions': (('open_discussion', 'Can create a discussion'), ('reply_discussion', 'Can reply discussion'), ('close_discussion', 'Can remove a discussion by setting its status as closed'))},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '1.5 \u7528\u6237_\u57fa\u672c\u4fe1\u606f', 'verbose_name_plural': '1.5 \u7528\u6237_\u57fa\u672c\u4fe1\u606f'},
        ),
    ]
