# Generated by Django 4.1.1 on 2022-11-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0026_privatedocument_efs_file_privatedocument_s3_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatedocument',
            name='file_count',
            field=models.IntegerField(help_text='count', null=True),
        ),
    ]
