# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_used', models.IntegerField(default=0, verbose_name='\u662f\u5426\u4f7f\u7528', choices=[(0, '\u672a\u4f7f\u7528'), (1, '\u5df2\u4f7f\u7528')])),
                ('is_active', models.IntegerField(default=1, verbose_name='\u662f\u5426\u4f5c\u5e9f', choices=[(0, '\u4f5c\u5e9f'), (1, '\u6709\u6548')])),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4f18\u60e0\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(default=order.models.three_day_hence, verbose_name='\u4f18\u60e0\u7ed3\u675f\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4f18\u60e0\u5238\u521b\u5efa\u65f6\u95f4', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '3.2 \u4f18\u60e0\u5238',
                'verbose_name_plural': '3.2 \u4f18\u60e0\u5238',
            },
        ),
        migrations.CreateModel(
            name='DiscountTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u4f18\u60e0\u5238\u540d\u79f0', blank=True)),
                ('use_condition', models.CharField(max_length=100, null=True, verbose_name='\u4f7f\u7528\u6761\u4ef6', blank=True)),
                ('use_range', models.CharField(max_length=100, null=True, verbose_name='\u4f7f\u7528\u8303\u56f4', blank=True)),
                ('agreement_type', models.IntegerField(default=0, verbose_name='\u4f18\u60e0\u5238\u7c7b\u522b', choices=[(0, '\u4f1a\u5458\u5408\u540c'), (1, '\u70b9\u64ad\u5408\u540c')])),
                ('fee', models.FloatField(default=5, verbose_name='\u4f18\u60e0\u4ef7\u683c')),
                ('limit_fee', models.FloatField(default=0, verbose_name='\u6700\u4f4e\u4f7f\u7528\u4ef7\u683c')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5408\u540c\u521b\u5efa\u65f6\u95f4', null=True)),
                ('role', models.ForeignKey(verbose_name='\u5141\u8bb8\u4f7f\u7528\u89d2\u8272', blank=True, to='api.Role', null=True)),
                ('tag', models.ForeignKey(verbose_name='\u5141\u8bb8\u4f7f\u7528\u7f51\u7ad9\u6807\u7b7e', blank=True, to='api.Tag', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '3.3 \u4f18\u60e0\u5238\u6a21\u677f',
                'verbose_name_plural': '3.3 \u4f18\u60e0\u5238\u6a21\u677f',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_alive', models.IntegerField(default=1, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')])),
                ('is_payment', models.IntegerField(default=0, verbose_name='\u652f\u4ed8\u72b6\u6001', choices=[(0, '\u5f85\u652f\u4ed8'), (1, '\u5df2\u652f\u4ed8')])),
                ('wx_out_trade_no', models.CharField(max_length=32, null=True, verbose_name='\u5fae\u4fe1_\u5546\u6237\u8ba2\u5355\u53f7', blank=True)),
                ('agreement_type', models.IntegerField(default=0, verbose_name='\u5408\u540c\u7c7b\u578b', choices=[(0, '\u4f1a\u5458\u5408\u540c'), (1, '\u70b9\u64ad\u5408\u540c')])),
                ('original_fee', models.FloatField(null=True, verbose_name='\u539f\u4ef7', blank=True)),
                ('payment_fee', models.FloatField(null=True, verbose_name='\u652f\u4ed8\u4ef7', blank=True)),
                ('create_time', models.DateTimeField(null=True, verbose_name='\u8ba2\u5355\u521b\u5efa\u65f6\u95f4')),
                ('play_num', models.IntegerField(null=True, verbose_name='\u5269\u4f59\u64ad\u653e\u6b21\u6570', blank=True)),
                ('start_time', models.DateTimeField(null=True, verbose_name='\u5408\u540c\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name='\u5408\u540c\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', blank=True, to='api.Article', null=True)),
                ('discount', models.ForeignKey(verbose_name='\u4f18\u60e0\u5238', blank=True, to='order.Discount', null=True)),
                ('renew_order', models.ForeignKey(verbose_name='\u7eed\u8d39\u7684\u5355\u53f7', blank=True, to='order.Order', null=True)),
                ('role', models.ForeignKey(verbose_name='\u89d2\u8272\u540d\u79f0', blank=True, to='api.Role', null=True)),
                ('tag', models.ForeignKey(verbose_name='\u7f51\u7ad9\u6807\u7b7e', blank=True, to='api.Tag', null=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', blank=True, to='api.User', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '3.1 \u8ba2\u5355',
                'verbose_name_plural': '3.1 \u8ba2\u5355',
            },
        ),
        migrations.AddField(
            model_name='discount',
            name='template',
            field=models.ForeignKey(verbose_name='\u4f18\u60e0\u5238\u7c7b\u578b', to='order.DiscountTemplate'),
        ),
        migrations.AddField(
            model_name='discount',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', to='api.User'),
        ),
    ]
