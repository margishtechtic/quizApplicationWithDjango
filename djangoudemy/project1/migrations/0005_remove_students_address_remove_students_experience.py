# Generated by Django 5.0.2 on 2024-03-01 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0004_attemps_log_attempted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='address',
        ),
        migrations.RemoveField(
            model_name='students',
            name='experience',
        ),
    ]