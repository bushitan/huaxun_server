# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_buy', models.IntegerField(default=1, verbose_name='\u4e70\u5165/\u5356\u51fa', choices=[(0, '\u5356\u51fa'), (1, '\u4e70\u5165')])),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u7b80\u8baf\u5185\u5bb9', blank=True)),
                ('phone', models.CharField(max_length=40, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('issue_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6587\u7ae0\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('tag', models.ForeignKey(verbose_name='\u6807\u7b7e', blank=True, to='api.Tag', null=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', blank=True, to='api.User', null=True)),
            ],
            options={
                'ordering': ['-issue_time'],
                'verbose_name': '\u4f9b\u6c42\u4fe1\u606f',
                'verbose_name_plural': '\u4f9b\u6c42\u4fe1\u606f',
            },
        ),
    ]
