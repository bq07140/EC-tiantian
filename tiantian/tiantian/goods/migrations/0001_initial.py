# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=50)),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gdesc', models.TextField(max_length=300)),
                ('gimgAdd', models.ImageField(upload_to=b'img')),
                ('gimgDetail', models.ImageField(upload_to=b'img')),
                ('isDelete', models.BooleanField(default=0)),
                ('gdetail', models.TextField(max_length=300)),
                ('gnews', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'goodsInfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=30)),
                ('title1', models.CharField(max_length=30)),
                ('title2', models.CharField(max_length=30)),
                ('title3', models.CharField(max_length=30)),
                ('tImgAdd', models.ImageField(upload_to=b'img')),
                ('typeId', models.IntegerField()),
                ('isDelete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'typeInfo',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.TypeInfo'),
        ),
    ]
