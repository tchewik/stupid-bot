# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tchotchka_with_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='ans',
            field=models.CharField(default=2, max_length=240, verbose_name='Елена парирует: '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bot',
            name='rep',
            field=models.CharField(verbose_name='Ваша реплика: ', max_length=240),
        ),
    ]
