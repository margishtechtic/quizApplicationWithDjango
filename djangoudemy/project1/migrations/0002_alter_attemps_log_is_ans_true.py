# Generated by Django 5.0.2 on 2024-02-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attemps_log',
            name='is_ans_true',
            field=models.BooleanField(default=False),
        ),
    ]
