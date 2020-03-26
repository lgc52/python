# Generated by Django 2.1.5 on 2019-03-25 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190315_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='wechat_friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_username', models.CharField(blank=True, max_length=255, null=True, verbose_name='好友账号')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('add_date', models.DateTimeField(default=datetime.datetime(2019, 3, 25, 14, 49, 23, 980750), verbose_name='添加时间')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 25, 14, 49, 23, 978237), verbose_name='任务添加时间'),
        ),
    ]
