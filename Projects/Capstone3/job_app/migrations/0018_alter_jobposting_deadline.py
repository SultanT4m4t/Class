# Generated by Django 5.1.7 on 2025-04-12 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0017_jobposting_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2025, 7, 11, 9, 24, 17, 986309, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
