# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-26 01:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('color', models.CharField(default='#ffffff', max_length=55)),
                ('color_class', models.CharField(default='white', max_length=55)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Color'),
        ),
    ]