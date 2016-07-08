# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tchotchka_with_bot', '0006_auto_20160708_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='guy',
        ),
    ]
