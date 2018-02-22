# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '3.2 \u533a\u57df',
                'verbose_name_plural': '3.2 \u533a\u57df',
            },
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('area', models.ForeignKey(related_name='father_tag', verbose_name='\u533a\u57df', blank=True, to='roster.Area', null=True)),
                ('buy', models.ManyToManyField(related_name='buy_tag', null=True, verbose_name='\u6c42\u8d2d', to='api.Tag', blank=True)),
                ('sell', models.ManyToManyField(related_name='sell_tag', null=True, verbose_name='\u4f9b\u5e94', to='api.Tag', blank=True)),
                ('tag', models.ForeignKey(related_name='father_tag', verbose_name='\u6240\u5c5e\u7f51\u7ad9', blank=True, to='api.Tag', null=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237ID', blank=True, to='api.User', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '3.1 \u8054\u7cfb\u4eba\u540d\u518c',
                'verbose_name_plural': '3.1 \u8054\u7cfb\u4eba\u540d\u518c',
            },
        ),
    ]
