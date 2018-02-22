# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('click_rate', models.IntegerField(default=568, verbose_name='\u70b9\u51fb\u7387')),
                ('is_top', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u7f6e\u9876', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')])),
                ('is_banner', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5e7f\u544a\u6587\u7ae0', choices=[(0, '\u4e00\u822c\u6587\u7ae0'), (1, '\u5e7f\u544a\u6587\u7ae0')])),
                ('is_show_title', models.IntegerField(default=1, verbose_name='\u5185\u5bb9\u662f\u5426\u663e\u793a\u6807\u9898', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('cover', models.CharField(max_length=1000, null=True, verbose_name='\u5c01\u9762\u56fe\u7247', blank=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('subtitle', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5b50\u6807\u9898', blank=True)),
                ('summary', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('source', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u6765\u6e90', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u6b63\u6587', blank=True)),
                ('content_width', models.IntegerField(default=750, null=True, verbose_name='\u6b63\u6587\u663e\u793a\u5bbd\u5ea6', blank=True)),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a\u6587\u7ae0', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('issue_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6587\u7ae0\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_show_audio', models.IntegerField(default=0, verbose_name='\u662f\u5426\u663e\u793a\u97f3\u9891', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('audio_src', models.CharField(max_length=1000, null=True, verbose_name='\u97f3\u9891\u5730\u5740(Url)', blank=True)),
                ('audio_poster', models.CharField(max_length=500, null=True, verbose_name='\u97f3\u9891\u5c01\u9762\u56fe(Url)', blank=True)),
                ('audio_name', models.CharField(max_length=100, null=True, verbose_name='\u97f3\u9891\u540d\u79f0', blank=True)),
                ('audio_author', models.CharField(max_length=100, null=True, verbose_name='\u97f3\u9891\u4f5c\u8005', blank=True)),
                ('is_show_video', models.IntegerField(default=0, verbose_name='\u662f\u5426\u663e\u793a\u89c6\u9891', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('video_src', models.CharField(max_length=1000, null=True, verbose_name='\u89c6\u9891\u5730\u5740(Url)', blank=True)),
                ('price', models.FloatField(default=6, null=True, verbose_name='\u666e\u901a\u70b9\u64ad\u5355\u4ef7')),
                ('is_show_navigate', models.IntegerField(default=0, verbose_name='\u662f\u5426\u8df3\u8f6c\u5230\u5c0f\u7a0b\u5e8f', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('navigate_appid', models.CharField(max_length=100, null=True, verbose_name='appid', blank=True)),
                ('navigate_path', models.CharField(max_length=100, null=True, verbose_name='\u9875\u9762\u8def\u5f84', blank=True)),
                ('navigate_data', models.CharField(max_length=100, null=True, verbose_name='\u4f20\u9012\u6570\u636e', blank=True)),
            ],
            options={
                'ordering': ['-issue_time', '-is_top'],
                'verbose_name': '1.1 \u6587\u7ae0',
                'verbose_name_plural': '1.1 \u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('cover', models.CharField(max_length=300, null=True, verbose_name='\u5c01\u9762\u56fe\u7247', blank=True)),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('is_swiper', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5934\u6761\u5e7f\u544a', choices=[(0, '\u4e00\u822c\u5e7f\u544a'), (1, '\u5934\u6761\u5e7f\u544a')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('article', models.ForeignKey(verbose_name='\u6240\u5c5e\u6587\u7ae0', to='api.Article', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '1.2 \u5e7f\u544a\u6761',
                'verbose_name_plural': '1.2 \u5e7f\u544a\u6761',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
            ],
            options={
                'verbose_name': '2.2 \u7528\u6237_\u4f01\u4e1a\u4fe1\u606f',
                'verbose_name_plural': '2.2 \u7528\u6237_\u4f01\u4e1a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HistoryUserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.IntegerField(default=0, verbose_name='\u5f00\u901a\u65b9\u5f0f', choices=[(0, '\u66f4\u6539'), (1, '\u589e\u52a0'), (2, '\u5220\u9664')])),
                ('create_type', models.IntegerField(default=0, verbose_name='\u5f00\u901a\u65b9\u5f0f', choices=[(0, '\u4eba\u5de5'), (1, '\u7cfb\u7edf')])),
                ('start_time', models.DateTimeField(null=True, verbose_name='\u5408\u540c\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name='\u5408\u540c\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('create_time', models.DateTimeField(null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('history_create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5386\u53f2\u8bb0\u5f55\u521b\u5efa\u65f6\u95f4', null=True)),
            ],
            options={
                'ordering': ['-history_create_time'],
                'verbose_name': '4.1 \u5408\u540c\u53d8\u66f4\u8bb0\u5f55',
                'verbose_name_plural': '4.1 \u5408\u540c\u53d8\u66f4\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='ImageMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='\u4e91\u5730\u5740', blank=True)),
                ('local_path', models.ImageField(upload_to=b'img/', verbose_name='\u56fe\u6807')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '1.5 \u56fe\u5e93',
                'verbose_name_plural': '1.5 \u56fe\u5e93',
            },
        ),
        migrations.CreateModel(
            name='PayBill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(null=True, verbose_name='\u652f\u4ed8\u5355\u4ef7', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8ba2\u5355\u521b\u5efa\u65f6\u95f4', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '4.3 \u652f\u4ed8\u8bb0\u5f55',
                'verbose_name_plural': '4.3 \u652f\u4ed8\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='RelArticleUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', to='api.Article')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '4.2 \u6d4f\u89c8\u8bb0\u5f55',
                'verbose_name_plural': '4.2 \u6d4f\u89c8\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('value', models.IntegerField(default=1, verbose_name='\u6743\u9650\u7b49\u7ea7')),
                ('price', models.FloatField(default=0, null=True, verbose_name='\u4f1a\u5458\u4ef7\u683c', blank=True)),
                ('image_url', models.CharField(max_length=500, null=True, verbose_name='\u4f1a\u5458\u56fe\u7247', blank=True)),
            ],
            options={
                'ordering': ['-value'],
                'verbose_name': '1.3 \u4f1a\u5458\u89d2\u8272',
                'verbose_name_plural': '1.3 \u4f1a\u5458\u89d2\u8272',
                'permissions': (('open_discussion', 'Can create a discussion'), ('reply_discussion', 'Can reply discussion'), ('close_discussion', 'Can remove a discussion by setting its status as closed')),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True)),
                ('des', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u5728\u9996\u9875\u663e\u793a\u6807\u7b7e', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_main', models.IntegerField(default=0, verbose_name='\u884c\u4e1a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_index', models.IntegerField(default=0, verbose_name='\u9996\u9875', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_match', models.IntegerField(default=0, verbose_name='\u4f9b\u6c42', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_ad', models.IntegerField(default=0, verbose_name='\u5e7f\u544a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_swiper', models.IntegerField(default=0, verbose_name='\u8f6e\u64ad', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_image_map', models.IntegerField(default=0, verbose_name='\u56fe\u5e93', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_meet', models.IntegerField(default=0, verbose_name='\u4f1a\u8bae', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_roster', models.IntegerField(default=0, verbose_name='\u5546\u5708', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('father', models.ForeignKey(verbose_name='\u7236\u76ee\u5f55', blank=True, to='api.Tag', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '1.3 \u6807\u7b7e',
                'verbose_name_plural': '1.3 \u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u5934\u50cf\u5730\u5740', blank=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u59d3\u540d', blank=True)),
                ('nick_name', models.CharField(max_length=100, null=True, verbose_name='\u5fae\u4fe1\u6635\u79f0', blank=True)),
                ('wx_id', models.CharField(max_length=100, null=True, verbose_name='\u5fae\u4fe1\u53f7', blank=True)),
                ('wx_open_id', models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1OpenID', blank=True)),
                ('wx_session_key', models.CharField(max_length=128, null=True, verbose_name='\u5fae\u4fe1SessionKey', blank=True)),
                ('wx_expires_in', models.FloatField(null=True, verbose_name='\u5fae\u4fe1SessionKey\u8fc7\u671f\u65f6\u95f4', blank=True)),
                ('session', models.CharField(max_length=128, null=True, verbose_name='Django\u7684session', blank=True)),
                ('expires', models.FloatField(null=True, verbose_name='Django\u7684session\u8fc7\u671f\u65f6\u95f4', blank=True)),
                ('uuid', models.CharField(max_length=32, null=True, verbose_name='uuid\u6807\u8bc6', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('identify_status', models.IntegerField(default=0, null=True, verbose_name='\u7ebf\u4e0b\u8ba4\u8bc1\u72b6\u6001', blank=True, choices=[(0, '\u672a\u63d0\u4ea4'), (1, '\u5df2\u63d0\u4ea4'), (2, '\u5ba1\u6838\u4e0d\u901a\u8fc7'), (3, '\u5ba1\u6838\u901a\u8fc7')])),
                ('phone', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('introduction', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True)),
                ('address', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('latitude', models.FloatField(default=0, verbose_name='\u7cbe\u5ea6')),
                ('longitude', models.FloatField(default=0, verbose_name='\u7ef4\u5ea6')),
                ('company', models.ForeignKey(verbose_name='\u6240\u5728\u516c\u53f8', blank=True, to='api.Company', null=True)),
                ('roster_image', models.ForeignKey(verbose_name='\u5546\u5708\u56fe\u7247', blank=True, to='api.ImageMap', null=True)),
            ],
            options={
                'verbose_name': '2.1 \u7528\u6237_\u57fa\u672c\u4fe1\u606f',
                'verbose_name_plural': '2.1 \u7528\u6237_\u57fa\u672c\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='relarticleuser',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to='api.User'),
        ),
        migrations.AddField(
            model_name='paybill',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to='api.User', null=True),
        ),
        migrations.AddField(
            model_name='imagemap',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6807\u7b7e', blank=True, to='api.Tag', null=True),
        ),
        migrations.AddField(
            model_name='historyuserrole',
            name='role',
            field=models.ForeignKey(verbose_name='\u89d2\u8272\u540d\u79f0', blank=True, to='api.Role', null=True),
        ),
        migrations.AddField(
            model_name='historyuserrole',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237\u540d\u79f0', blank=True, to='api.User', null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u6807\u7b7e', to='api.Tag', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='cover_image',
            field=models.ForeignKey(verbose_name='\u9009\u62e9\u5c01\u9762\u56fe\u7247', blank=True, to='api.ImageMap', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='role',
            field=models.ForeignKey(default=1, verbose_name='\u6d4f\u89c8\u6743\u9650', to='api.Role'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6807\u7b7e', blank=True, to='api.Tag', null=True),
        ),
    ]
