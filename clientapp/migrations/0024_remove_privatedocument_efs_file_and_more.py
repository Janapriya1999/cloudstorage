# Generated by Django 4.1.1 on 2022-11-10 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0023_privatedocument_file_size_privatedocument_file_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatedocument',
            name='efs_file',
        ),
        migrations.RemoveField(
            model_name='privatedocument',
            name='s3_files',
        ),
    ]
