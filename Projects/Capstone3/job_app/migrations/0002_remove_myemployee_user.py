# Generated by Django 5.1.7 on 2025-04-10 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myemployee',
            name='user',
        ),
    ]
