# Generated by Django 3.0.7 on 2021-01-03 10:08

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('Model5', '0009_auto_20201230_2051'),
        ]

    operations = [
        migrations.AddField(
                model_name='luruye',
                name='neirongshuoming',
                field=models.CharField(default='', max_length=100, null=True,
                                       verbose_name='工作要求说明'),
                ),
        migrations.AddField(
                model_name='luruye',
                name='zhouqi',
                field=models.CharField(default='', max_length=100, null=True, verbose_name='工作周期'),
                ),
        migrations.AddField(
                model_name='zhuye',
                name='neirongshuoming',
                field=models.CharField(default='', max_length=100, null=True,
                                       verbose_name='工作要求说明'),
                ),
        migrations.AddField(
                model_name='zhuye',
                name='zhouqi',
                field=models.CharField(default='', max_length=100, null=True, verbose_name='工作周期'),
                ),
        ]
