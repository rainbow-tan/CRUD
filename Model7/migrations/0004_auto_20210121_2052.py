# Generated by Django 3.0.7 on 2021-01-21 12:52

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('Model7', '0003_auto_20210117_1556'),
        ]

    operations = [
        migrations.CreateModel(
                name='DataTable',
                fields=[
                    ('auto_id',
                     models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                    ('xianbie',
                     models.CharField(default='', max_length=100, null=True, verbose_name='线别')),
                    ('chejian',
                     models.CharField(default='', max_length=100, null=True, verbose_name='综合车间')),
                    ('didian',
                     models.CharField(default='', max_length=100, null=True, verbose_name='使用地点')),
                    ('zongcheng', models.CharField(default='', max_length=100, null=True,
                                                   verbose_name='计量器具总称')),
                    ('mingcheng', models.CharField(default='', max_length=100, null=True,
                                                   verbose_name='计量器具名称')),
                    ('bianhao',
                     models.CharField(default='', max_length=100, null=True, verbose_name='出产编号')),
                    ('guige',
                     models.CharField(default='', max_length=100, null=True, verbose_name='规格型号')),
                    ('dengji',
                     models.CharField(default='', max_length=100, null=True, verbose_name='准确度等级')),
                    ('fanwei', models.CharField(default='', max_length=100, null=True,
                                                verbose_name='测量范围(mm)')),
                    ('changjia',
                     models.CharField(default='', max_length=100, null=True, verbose_name='制造厂家')),
                    ('zhuanye',
                     models.CharField(default='', max_length=100, null=True, verbose_name='专业')),
                    ('fuzeren',
                     models.CharField(default='', max_length=100, null=True, verbose_name='保管负责人')),
                    ('riqi',
                     models.CharField(default='', max_length=100, null=True, verbose_name='检定日期')),
                    ('xiaciriqi', models.CharField(default='', max_length=100, null=True,
                                                   verbose_name='下次检定日期')),
                    ('zhouqi',
                     models.CharField(default='', max_length=100, null=True, verbose_name='检定周期')),
                    ('dangqianzhuangtai',
                     models.CharField(default='', max_length=100, null=True, verbose_name='当前状态')),
                    ('yibiaozhuangtai',
                     models.CharField(default='', max_length=100, null=True, verbose_name='仪表状态')),
                    ('beizhu',
                     models.CharField(default='', max_length=100, null=True, verbose_name='备注')),
                    ('caozuo',
                     models.CharField(default='', max_length=100, null=True, verbose_name='操作')),
                    ],
                ),
        migrations.CreateModel(
                name='XianbieChejianChenZhan',
                fields=[
                    ('auto_id',
                     models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                    ('xianbie',
                     models.CharField(default='', max_length=100, null=True, verbose_name='线别')),
                    ('chejian',
                     models.CharField(default='', max_length=100, null=True, verbose_name='综合车间')),
                    ('chezhan', models.CharField(default='', max_length=100, null=True, unique=True,
                                                 verbose_name='车站名称')),
                    ],
                ),
        migrations.DeleteModel(
                name='XianbieChejian',
                ),
        migrations.DeleteModel(
                name='Yiqiyibiaotaizhang',
                ),
        ]
