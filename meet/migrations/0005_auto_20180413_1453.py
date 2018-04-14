# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0004_delete_articlestyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelibrary',
            name='local_path',
            field=models.ImageField(default=b'', upload_to=b'img/', verbose_name='\u56fe\u6807'),
        ),
    ]
