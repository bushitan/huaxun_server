# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0003_auto_20180227_1035'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleStyle',
        ),
    ]
