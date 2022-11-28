# Generated by Django 4.1.1 on 2022-11-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0017_privatedocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatedocument',
            name='privateuploadfilestatus',
            field=models.CharField(default='pending', help_text='file_status', max_length=300),
        ),
        migrations.AddField(
            model_name='privatedocument',
            name='privateuploadfiletransferstatus',
            field=models.CharField(default='pending', help_text='file_transfer_status', max_length=300),
        ),
    ]
