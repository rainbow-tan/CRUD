# Generated by Django 3.0.8 on 2021-01-28 08:56

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('Model2', '0001_initial'),
        ]

    operations = [
        migrations.AlterField(
                model_name='datatable',
                name='auto_id',
                field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field1',
                field=models.CharField(max_length=200, verbose_name='线别'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field2',
                field=models.CharField(max_length=200, verbose_name='综合车间'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field23',
                field=models.CharField(max_length=200, verbose_name='行别'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field3',
                field=models.CharField(max_length=200, verbose_name='车站及区间名称'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field30',
                field=models.CharField(max_length=200, verbose_name='电务段名称'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field31',
                field=models.CharField(max_length=200, verbose_name='自动闭塞制式'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field32',
                field=models.CharField(max_length=200, verbose_name='轨道电路制式'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field33',
                field=models.CharField(max_length=200, verbose_name='自闭区间'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field34',
                field=models.CharField(max_length=200, verbose_name='车站联锁制式'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field35',
                field=models.CharField(max_length=200, verbose_name='区间轨道电路名称'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field36',
                field=models.CharField(max_length=200, verbose_name='是否站联区段'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field37',
                field=models.CharField(max_length=200, verbose_name='标称载频'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field38',
                field=models.CharField(max_length=200, verbose_name='区段长度(m)'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field39',
                field=models.CharField(max_length=200, verbose_name='电容数量'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field40',
                field=models.CharField(max_length=200, verbose_name='防护信号机名称'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field41',
                field=models.CharField(max_length=200, verbose_name='是否容许信号'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field42',
                field=models.CharField(max_length=200, verbose_name='方向电路制式'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field43',
                field=models.CharField(max_length=200, verbose_name='发送冗余方式'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field44',
                field=models.CharField(max_length=200, verbose_name='接收冗余方式'),
                ),
        migrations.AlterField(
                model_name='datatable',
                name='field45',
                field=models.CharField(max_length=200, verbose_name='大修年'),
                ),
        migrations.AlterField(
                model_name='field36table',
                name='auto_id',
                field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
                ),
        migrations.AlterField(
                model_name='field36table',
                name='field1',
                field=models.CharField(max_length=200, verbose_name='是否站联区段'),
                ),
        migrations.AlterField(
                model_name='field37table',
                name='auto_id',
                field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
                ),
        migrations.AlterField(
                model_name='field37table',
                name='field1',
                field=models.CharField(max_length=200, verbose_name='标称载频'),
                ),
        migrations.AlterField(
                model_name='field41table',
                name='auto_id',
                field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
                ),
        migrations.AlterField(
                model_name='field41table',
                name='field1',
                field=models.CharField(max_length=200, verbose_name='是否容许信号'),
                ),
        migrations.AlterField(
                model_name='field42table',
                name='auto_id',
                field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
                ),
        migrations.AlterField(
                model_name='field42table',
                name='field1',
                field=models.CharField(max_length=200, verbose_name='方向电路制式'),
                ),
        ]
