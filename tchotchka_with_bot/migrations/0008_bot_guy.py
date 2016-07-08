# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tchotchka_with_bot', '0007_remove_bot_guy'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='guy',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
    ]
