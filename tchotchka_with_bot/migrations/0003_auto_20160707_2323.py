# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tchotchka_with_bot', '0002_auto_20160707_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='ans',
            field=models.CharField(max_length=240, verbose_name='Елена парирует'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='rep',
            field=models.CharField(max_length=240, verbose_name='Ваша реплика'),
        ),
    ]
