# Generated by Django 4.1.1 on 2022-10-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0005_rename_client_file_upload_id_filesmodel_video_uploader_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesmodel',
            name='file_size',
            field=models.IntegerField(default=1, null=True),
        ),
    ]