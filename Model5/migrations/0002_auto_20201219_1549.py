# Generated by Django 3.0.7 on 2020-12-19 07:49

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('Model5', '0001_initial'),
        ]

    operations = [
        migrations.AlterField(
                model_name='chenjian_chezhan',
                name='chezhan',
                field=models.CharField(max_length=100, unique=True, verbose_name='车站'),
                ),
        migrations.AlterField(
                model_name='xiangmu_gongzuoneirong',
                name='gongzuoneirong',
                field=models.CharField(max_length=100, unique=True, verbose_name='工作内容'),
                ),
        ]
