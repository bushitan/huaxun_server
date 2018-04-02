# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import meet_sign.models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0004_delete_articlestyle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wx_union_id', models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1UnionID', blank=True)),
                ('wx_open_id', models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1OpenID', blank=True)),
                ('session', models.CharField(max_length=128, null=True, verbose_name='Django\u7684session', blank=True)),
                ('uuid', models.CharField(max_length=32, null=True, verbose_name='uuid\u6807\u8bc6', blank=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u59d3\u540d', blank=True)),
                ('nick_name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5fae\u4fe1\u6635\u79f0', blank=True)),
                ('logo', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u5934\u50cf', blank=True)),
                ('male', models.BooleanField(default=1, verbose_name='\u6027\u522b', choices=[(0, '\u5973'), (1, '\u7537')])),
                ('company', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u4f01\u4e1a\u540d\u79f0', blank=True)),
                ('phone', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u7535\u8bdd', blank=True)),
                ('position', models.CharField(max_length=100, null=True, verbose_name='\u804c\u52a1', blank=True)),
                ('remark', models.CharField(max_length=100, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.5.1 \u53c2\u4f1a\u4eba\u5458\u8868',
                'verbose_name_plural': '6.5.1 \u53c2\u4f1a\u4eba\u5458\u8868',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f-\u9879\u76ee\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0-\u9879\u76ee\u540d\u79f0', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8d39\u7528\u8bf4\u660e', blank=True)),
                ('unit_price', models.FloatField(default=0, verbose_name='\u5355\u4ef7')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('meet', models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.6 \u8d39\u7528',
                'verbose_name_plural': '6.6 \u8d39\u7528',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_used', models.IntegerField(default=1, verbose_name='\u662f\u5426\u4f7f\u7528', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_active', models.IntegerField(default=1, verbose_name='\u662f\u5426\u4f5c\u5e9f', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4f18\u60e0\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(default=meet_sign.models.three_day_hence, verbose_name='\u4f18\u60e0\u7ed3\u675f\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4f18\u60e0\u5238\u521b\u5efa\u65f6\u95f4')),
                ('attendee', models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', blank=True, to='meet_sign.Attendee', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.8 \u4f18\u60e0\u5238',
                'verbose_name_plural': '6.8 \u4f18\u60e0\u5238',
            },
        ),
        migrations.CreateModel(
            name='DiscountTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u4f18\u60e0\u5238\u540d\u79f0', blank=True)),
                ('use_condition', models.CharField(max_length=100, null=True, verbose_name='\u4f7f\u7528\u6761\u4ef6', blank=True)),
                ('use_range', models.CharField(max_length=100, null=True, verbose_name='\u4f7f\u7528\u8303\u56f4', blank=True)),
                ('fee', models.FloatField(default=5, verbose_name='\u4f18\u60e0\u4ef7\u683c')),
                ('limit_fee', models.FloatField(default=0, verbose_name='\u6700\u4f4e\u4f7f\u7528\u4ef7\u683c')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.7 \u4f18\u60e0\u5238\u6a21\u677f',
                'verbose_name_plural': '6.7 \u4f18\u60e0\u5238\u6a21\u677f',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_alive', models.IntegerField(default=1, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b'), (3, '\u65e0\u610f\u4e49')])),
                ('is_pay', models.IntegerField(default=0, verbose_name='\u652f\u4ed8\u72b6\u6001', choices=[(0, '\u672a\u652f\u4ed8'), (1, '\u5df2\u652f\u4ed8')])),
                ('wx_out_trade_no', models.CharField(max_length=32, null=True, verbose_name='\u5fae\u4fe1_\u5546\u6237\u8ba2\u5355\u53f7', blank=True)),
                ('origin_price', models.FloatField(default=0, verbose_name='\u539f\u59cb\u4ef7\u683c')),
                ('pay_price', models.FloatField(default=0, verbose_name='\u652f\u4ed8\u4ef7\u683c')),
                ('remark', models.CharField(max_length=100, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('discount', models.ForeignKey(verbose_name='\u4f18\u60e0\u5238', blank=True, to='meet_sign.Discount', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.5 \u8ba2\u5355',
                'verbose_name_plural': '6.5 \u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_alive', models.BooleanField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b'), (3, '\u65e0\u610f\u4e49')])),
                ('alive_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6709\u6548\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('attendee', models.ForeignKey(related_name='order_user', verbose_name='\u7528\u6237', blank=True, to='meet_sign.Attendee', null=True)),
                ('cost', models.ForeignKey(verbose_name='\u4f1a\u8bae\u652f\u4ed8\u9879\u76ee', blank=True, to='meet_sign.Cost', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.6 \u53c2\u4f1a\u62a5\u540d',
                'verbose_name_plural': '6.6 \u53c2\u4f1a\u62a5\u540d',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='sign',
            field=models.ForeignKey(verbose_name='\u53c2\u4f1a\u62a5\u540d', blank=True, to='meet_sign.Sign', null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='template',
            field=models.ForeignKey(verbose_name='\u4f18\u60e0\u5238\u7c7b\u578b', to='meet_sign.DiscountTemplate'),
        ),
    ]
