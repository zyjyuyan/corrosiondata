# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('chemicalid', models.IntegerField()),
                ('chemicalname', models.CharField(max_length=40)),
                ('P', models.CharField(max_length=40)),
                ('C', models.CharField(max_length=40)),
                ('S', models.CharField(max_length=40)),
                ('Si', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CorrosionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('corrosionid', models.IntegerField()),
                ('environmentid', models.IntegerField()),
                ('chemicalid', models.IntegerField()),
                ('starttime', models.DateField()),
                ('endtime', models.DateField()),
                ('corrosionrate', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('environmentid', models.IntegerField()),
                ('time', models.DateField()),
                ('location', models.CharField(max_length=40)),
                ('sunshine', models.CharField(max_length=40)),
                ('hcl', models.CharField(max_length=40)),
                ('so2', models.CharField(max_length=40)),
                ('ph', models.CharField(max_length=40)),
                ('rain', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]