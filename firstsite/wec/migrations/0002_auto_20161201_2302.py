# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='pic',
            field=models.ImageField(null=True, upload_to=b'pic_folder/', blank=True),
        ),
    ]
