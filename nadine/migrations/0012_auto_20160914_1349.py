# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 20:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nadine', '0011_rename_DailyLog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coworkingday',
            options={'ordering': ['-visit_date', '-created_ts'], 'verbose_name': 'Coworking Day'},
        ),
        migrations.RenameField(
            model_name='coworkingday',
            old_name='created',
            new_name='created_ts',
        ),
        migrations.AddField(
            model_name='event',
            name='paid_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='charge',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
