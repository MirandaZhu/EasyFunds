# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_attachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='guide',
            new_name='guides',
        ),
        migrations.RemoveField(
            model_name='event',
            name='attachment',
        ),
        migrations.AddField(
            model_name='event',
            name='attachments',
            field=models.ManyToManyField(blank=True, related_name='events', to='events.Attachment'),
        ),
    ]
