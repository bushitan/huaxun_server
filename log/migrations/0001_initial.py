# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_read', models.IntegerField(default=1, verbose_name='\u5df2\u6d4f\u89c8/\u5f85\u4ed8\u8d39', choices=[(0, '\u5f85\u4ed8\u8d39'), (1, '\u5df2\u6d4f\u89c8')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('article', models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='api.Article', null=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', blank=True, to='api.User', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u6587\u7ae0\u70b9\u51fb\u7edf\u8ba1',
                'verbose_name_plural': '\u6587\u7ae0\u70b9\u51fb\u7edf\u8ba1',
            },
        ),
    ]
