# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meet_sign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f-\u9879\u76ee\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0-\u9879\u76ee\u540d\u79f0', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8d39\u7528\u8bf4\u660e', blank=True)),
                ('unit_price', models.FloatField(default=0, verbose_name='\u5355\u4ef7')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.6 \u8d39\u7528',
                'verbose_name_plural': '6.6 \u8d39\u7528',
            },
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_alive', models.BooleanField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')])),
                ('alive_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6709\u6548\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.6 \u53c2\u4f1a\u62a5\u540d',
                'verbose_name_plural': '6.6 \u53c2\u4f1a\u62a5\u540d',
            },
        ),
        migrations.RemoveField(
            model_name='bill',
            name='meet',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='order',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='order',
            name='num',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='attendee',
            name='male',
            field=models.BooleanField(default=1, verbose_name='\u6027\u522b', choices=[(0, '\u5973'), (1, '\u7537')]),
        ),
        migrations.AddField(
            model_name='attendee',
            name='position',
            field=models.CharField(max_length=100, null=True, verbose_name='\u804c\u52a1', blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='session',
            field=models.CharField(max_length=128, null=True, verbose_name='Django\u7684session', blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='uuid',
            field=models.CharField(max_length=32, null=True, verbose_name='uuid\u6807\u8bc6', blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='wx_open_id',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1OpenID', blank=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='wx_union_id',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1UnionID', blank=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='attendee',
            field=models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', blank=True, to='meet_sign.Attendee', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_alive',
            field=models.IntegerField(default=1, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')]),
        ),
        migrations.AddField(
            model_name='order',
            name='is_payment',
            field=models.IntegerField(default=0, verbose_name='\u652f\u4ed8\u72b6\u6001', choices=[(0, '\u5f85\u652f\u4ed8'), (1, '\u5df2\u652f\u4ed8')]),
        ),
        migrations.AddField(
            model_name='order',
            name='origin_price',
            field=models.FloatField(default=0, verbose_name='\u539f\u59cb\u4ef7\u683c'),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_price',
            field=models.FloatField(default=0, verbose_name='\u652f\u4ed8\u4ef7\u683c'),
        ),
        migrations.AddField(
            model_name='order',
            name='wx_out_trade_no',
            field=models.CharField(max_length=32, null=True, verbose_name='\u5fae\u4fe1_\u5546\u6237\u8ba2\u5355\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='company',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u4f01\u4e1a\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u59d3\u540d1', blank=True),
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.AddField(
            model_name='sign',
            name='attendee',
            field=models.ForeignKey(related_name='order_user', verbose_name='\u7528\u6237', blank=True, to='meet_sign.Attendee', null=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='cost',
            field=models.ForeignKey(verbose_name='\u4f1a\u8bae\u652f\u4ed8\u9879\u76ee', blank=True, to='meet_sign.Cost', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='sign',
            field=models.ForeignKey(verbose_name='\u53c2\u4f1a\u62a5\u540d', blank=True, to='meet_sign.Sign', null=True),
        ),
    ]
