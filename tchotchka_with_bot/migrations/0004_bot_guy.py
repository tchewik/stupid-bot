# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tchotchka_with_bot', '0003_auto_20160707_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='guy',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
