# Generated by Django 3.2.15 on 2022-09-22 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ial_app', '0006_auto_20220704_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciselist',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='updated_at',
        ),
    ]
