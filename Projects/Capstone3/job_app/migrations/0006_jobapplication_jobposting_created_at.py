# Generated by Django 5.1.7 on 2025-04-12 08:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_jobposting'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='jobposting',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
