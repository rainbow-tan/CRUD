# Generated by Django 3.0.7 on 2020-09-03 13:06

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ]

    operations = [
        migrations.CreateModel(
                name='DataTable',
                fields=[
                    ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                    ('field30', models.CharField(max_length=200)),
                    ('field1', models.CharField(max_length=200)),
                    ('field2', models.CharField(max_length=200)),
                    ('field23', models.CharField(max_length=200)),
                    ('field31', models.CharField(max_length=200)),
                    ('field32', models.CharField(max_length=200)),
                    ('field33', models.CharField(max_length=200)),
                    ('field3', models.CharField(max_length=200)),
                    ('field34', models.CharField(max_length=200)),
                    ('field35', models.CharField(max_length=200)),
                    ('field36', models.CharField(max_length=200)),
                    ('field37', models.CharField(max_length=200)),
                    ('field38', models.CharField(max_length=200)),
                    ('field39', models.CharField(max_length=200)),
                    ('field40', models.CharField(max_length=200)),
                    ('field41', models.CharField(max_length=200)),
                    ('field42', models.CharField(max_length=200)),
                    ('field43', models.CharField(max_length=200)),
                    ('field44', models.CharField(max_length=200)),
                    ('field45', models.CharField(max_length=200)),
                    ],
                ),
        migrations.CreateModel(
                name='Field36Table',
                fields=[
                    ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                    ('field1', models.CharField(max_length=200)),
                    ],
                ),
        migrations.CreateModel(
                name='Field37Table',
                fields=[
                    ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                    ('field1', models.CharField(max_length=200)),
                    ],
                ),
        migrations.CreateModel(
                name='Field41Table',
                fields=[
                    ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                    ('field1', models.CharField(max_length=200)),
                    ],
                ),
        migrations.CreateModel(
                name='Field42Table',
                fields=[
                    ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                    ('field1', models.CharField(max_length=200)),
                    ],
                ),
        ]
