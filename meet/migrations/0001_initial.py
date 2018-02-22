# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('summary', models.CharField(max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8be6\u7ec6\u63cf\u8ff0', blank=True)),
                ('footer', models.CharField(max_length=100, null=True, verbose_name='\u9875\u811a', blank=True)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.1 \u76ee\u5f55 -- \u65e5\u7a0b',
                'verbose_name_plural': '6.1 \u76ee\u5f55 -- \u65e5\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='ArticleLibrary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a\u6587\u7ae0', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('click_rate', models.IntegerField(default=8965, verbose_name='\u70b9\u51fb\u7387')),
                ('is_top', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u7f6e\u9876', choices=[(0, '\u4e00\u822c'), (1, '\u7f6e\u9876')])),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('subtitle', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5b50\u6807\u9898', blank=True)),
                ('summary', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('source', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u6765\u6e90', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u6b63\u6587', blank=True)),
                ('content_width', models.IntegerField(default=750, null=True, verbose_name='\u6b63\u6587\u663e\u793a\u5bbd\u5ea6', blank=True)),
                ('issue_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6587\u7ae0\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('audio_src', models.CharField(max_length=1000, null=True, verbose_name='\u97f3\u9891\u5730\u5740(Url)', blank=True)),
                ('audio_poster', models.CharField(max_length=500, null=True, verbose_name='\u97f3\u9891\u5c01\u9762\u56fe(Url)', blank=True)),
                ('audio_name', models.CharField(max_length=100, null=True, verbose_name='\u97f3\u9891\u540d\u79f0', blank=True)),
                ('audio_author', models.CharField(max_length=100, null=True, verbose_name='\u97f3\u9891\u4f5c\u8005', blank=True)),
                ('video_src', models.CharField(max_length=1000, null=True, verbose_name='\u89c6\u9891\u5730\u5740(Url)', blank=True)),
                ('address', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('work_date', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5de5\u4f5c\u65f6\u95f4', blank=True)),
                ('phone', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u7535\u8bdd', blank=True)),
                ('introduction', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u7b80\u4ecb', blank=True)),
            ],
            options={
                'ordering': ['-issue_time', '-is_top'],
                'verbose_name': '6.4 \u6587\u7ae0',
                'verbose_name_plural': '6.4 \u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='ArticleStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u524d\u53f0\u9875\u9762\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(default=b'', max_length=32, null=True, verbose_name='admin\u9875\u9762\u540d\u79f0', blank=True)),
                ('mark', models.IntegerField(default=0, verbose_name='\u9875\u9762\u5bf9\u5e94\u7684\u6807\u8bb0')),
                ('fieldsets', models.TextField(default=b'', null=True, verbose_name='admin\u9875\u9762\u914d\u7f6e', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.3 \u6587\u7ae0\u6837\u5f0f',
                'verbose_name_plural': '6.3 \u6587\u7ae0\u6837\u5f0f',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u59d3\u540d', blank=True)),
                ('company', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u516c\u53f8', blank=True)),
                ('introduction', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='meet.ArticleLibrary', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.1 \u76ee\u5f55 -- \u5609\u5bbe',
                'verbose_name_plural': '6.1 \u76ee\u5f55 -- \u5609\u5bbe',
            },
        ),
        migrations.CreateModel(
            name='ImageLibrary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='\u4e91\u5730\u5740', blank=True)),
                ('style', models.IntegerField(default=1, verbose_name='\u7c7b\u522b', choices=[(1, '\u5c01\u9762'), (2, '\u5934\u50cf')])),
                ('local_path', models.ImageField(upload_to=b'img/', verbose_name='\u56fe\u6807')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '6.2 \u4f1a\u8bae\u56fe\u5e93',
                'verbose_name_plural': '6.2 \u4f1a\u8bae\u56fe\u5e93',
            },
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.IntegerField(default=2, verbose_name='\u7c7b\u522b', choices=[(1, b'\xe4\xb8\xbb\xe4\xbc\x9a\xe8\xae\xae'), (2, b'\xe6\x97\xa5\xe7\xa8\x8b'), (3, b'\xe5\x88\x86\xe4\xbc\x9a\xe5\x9c\xba')])),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u4f1a\u8bae\u540d\u79f0', blank=True)),
                ('des', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name='\u4f1a\u52a1\u72b6\u6001', choices=[(0, '\u672a\u53ec\u5f00'), (1, '\u5f00\u59cb'), (2, '\u5df2\u7ed3\u675f')])),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('address', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('latitude', models.FloatField(default=0, verbose_name='\u7cbe\u5ea6')),
                ('longitude', models.FloatField(default=0, verbose_name='\u7ef4\u5ea6')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('father', models.ForeignKey(verbose_name='\u7236\u4f1a\u8bae', blank=True, to='meet.Meet', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '6.1 \u4e3b\u4f1a\u8bae',
                'verbose_name_plural': '6.1 \u4e3b\u4f1a\u8bae',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('summary', models.CharField(max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8be6\u7ec6\u63cf\u8ff0', blank=True)),
                ('footer', models.CharField(max_length=100, null=True, verbose_name='\u9875\u811a', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='meet.ArticleLibrary', null=True)),
                ('cover_image', models.ForeignKey(verbose_name='\u5c01\u9762\u56fe\u7247', blank=True, to='meet.ImageLibrary', null=True)),
                ('meet', models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.1 \u76ee\u5f55 -- \u65b0\u95fb',
                'verbose_name_plural': '6.1 \u76ee\u5f55 -- \u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('summary', models.CharField(max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8be6\u7ec6\u63cf\u8ff0', blank=True)),
                ('footer', models.CharField(max_length=100, null=True, verbose_name='\u9875\u811a', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='meet.ArticleLibrary', null=True)),
                ('cover_image', models.ForeignKey(verbose_name='\u5c01\u9762\u56fe\u7247', blank=True, to='meet.ImageLibrary', null=True)),
                ('meet', models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.1 \u76ee\u5f55 -- \u666f\u70b9',
                'verbose_name_plural': '6.1 \u76ee\u5f55 -- \u666f\u70b9',
            },
        ),
        migrations.CreateModel(
            name='Swiper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('style', models.IntegerField(default=1, verbose_name='\u4f1a\u52a1\u72b6\u6001', choices=[(1, b'\xe6\x97\xa5\xe7\xa8\x8b'), (2, b'\xe6\x96\xb0\xe9\x97\xbb')])),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('summary', models.CharField(max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8be6\u7ec6\u63cf\u8ff0', blank=True)),
                ('footer', models.CharField(max_length=100, null=True, verbose_name='\u9875\u811a', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='meet.ArticleLibrary', null=True)),
                ('cover_image', models.ForeignKey(verbose_name='\u5c01\u9762\u56fe\u7247', blank=True, to='meet.ImageLibrary', null=True)),
                ('meet', models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.1 \u8f6e\u64ad\u56fe',
                'verbose_name_plural': '6.1 \u8f6e\u64ad\u56fe',
            },
        ),
        migrations.AddField(
            model_name='guest',
            name='logo_image',
            field=models.ForeignKey(verbose_name='\u5609\u5bbe\u5934\u50cf', blank=True, to='meet.ImageLibrary', null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='meet',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True),
        ),
        migrations.AddField(
            model_name='articlelibrary',
            name='style',
            field=models.ForeignKey(verbose_name='\u9875\u9762\u7c7b\u522b', blank=True, to='meet.ArticleStyle', null=True),
        ),
        migrations.AddField(
            model_name='agenda',
            name='article',
            field=models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='meet.ArticleLibrary', null=True),
        ),
        migrations.AddField(
            model_name='agenda',
            name='meet',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u4f1a\u8bae', blank=True, to='meet.Meet', null=True),
        ),
    ]
