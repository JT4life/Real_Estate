# Generated by Django 2.2 on 2020-06-12 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20200611_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 16, 41, 17, 264205, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='properties',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 16, 41, 17, 264205, tzinfo=utc)),
        ),
    ]
