# Generated by Django 4.1.1 on 2022-10-21 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0006_alter_filesmodel_file_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesmodel',
            name='file_duration',
        ),
        migrations.RemoveField(
            model_name='filesmodel',
            name='file_size',
        ),
        migrations.RemoveField(
            model_name='filesmodel',
            name='file_type',
        ),
    ]
