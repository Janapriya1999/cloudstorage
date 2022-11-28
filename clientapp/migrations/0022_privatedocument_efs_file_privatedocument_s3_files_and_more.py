# Generated by Django 4.1.1 on 2022-11-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0021_alter_clientmodel_client_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatedocument',
            name='efs_file',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='privatedocument',
            name='s3_files',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='client_photo',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
