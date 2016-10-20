# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import firstsite.wec.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic', models.ImageField(null=True, upload_to=firstsite.wec.models.image_name, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Employee')),
                ('clock', models.CharField(default=b'0', max_length=10, verbose_name=b'Clock')),
                ('tpe', models.CharField(default=b'', max_length=200, verbose_name=b'tpe', blank=True)),
                ('db', models.CharField(default=b'', max_length=200, verbose_name=b'db', blank=True)),
                ('entry', models.CharField(default=b'', max_length=200, verbose_name=b'entry', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'Name')),
                ('user', models.CharField(default=b'', max_length=30, verbose_name=b'User Name')),
                ('type', models.CharField(default=b'admin', max_length=30)),
                ('password', models.CharField(default=b'', max_length=30, verbose_name=b'Password')),
                ('password_v', models.CharField(default=b'', max_length=30, verbose_name=b'Password Again')),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('address', models.CharField(default=b'', max_length=70, verbose_name=b'Address')),
                ('city', models.CharField(default=b'', max_length=70, verbose_name=b'City')),
                ('country', models.CharField(default=b'', max_length=70, verbose_name=b'Country')),
                ('code', models.CharField(default=b'', max_length=70, verbose_name=b'Zip')),
                ('phone', models.CharField(default=b'', max_length=70, verbose_name=b'Phone')),
                ('signup', models.DateField(default=datetime.datetime.now, editable=False)),
                ('status', models.IntegerField(default=0)),
                ('DB', models.CharField(max_length=50, verbose_name=b'Business')),
            ],
        ),
        migrations.CreateModel(
            name='Members_Features',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feature', models.CharField(max_length=70, verbose_name=b'Feature')),
                ('feature_name', models.CharField(default=b'', max_length=50, verbose_name=b'Feature Name')),
                ('DB', models.CharField(max_length=50, verbose_name=b'Business')),
            ],
        ),
        migrations.CreateModel(
            name='membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('db', models.CharField(max_length=200)),
                ('app', models.CharField(max_length=200)),
                ('app_date', models.DateField(verbose_name=b'')),
            ],
        ),
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(default=b'', max_length=30, verbose_name=b'User Id')),
                ('password', models.CharField(default=b'', max_length=30, verbose_name=b'Password')),
                ('DB', models.CharField(max_length=50, verbose_name=b'Business')),
            ],
        ),
        migrations.CreateModel(
            name='temp1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('clock', models.IntegerField(default=0)),
                ('tpe', models.CharField(max_length=200)),
                ('db', models.CharField(max_length=200)),
                ('entry', models.CharField(max_length=200)),
            ],
        ),
    ]
