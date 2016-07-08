# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tchotchka_with_bot', '0005_auto_20160708_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='guy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
