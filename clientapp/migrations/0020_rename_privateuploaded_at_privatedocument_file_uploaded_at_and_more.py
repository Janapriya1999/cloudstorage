# Generated by Django 4.1.1 on 2022-11-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0019_rename_privateuploadfile_privatedocument_uploaded_video_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatedocument',
            old_name='privateuploaded_at',
            new_name='file_uploaded_at',
        ),
        migrations.RenameField(
            model_name='privatedocument',
            old_name='privateupload_file',
            new_name='upload_file',
        ),
        migrations.RenameField(
            model_name='privatedocument',
            old_name='privateuploadname',
            new_name='upload_file_name',
        ),
        migrations.RenameField(
            model_name='privatedocument',
            old_name='privateuploadmessage',
            new_name='upload_message',
        ),
        migrations.RenameField(
            model_name='privatedocument',
            old_name='privateclient',
            new_name='video_uploader',
        ),
        migrations.RemoveField(
            model_name='privatedocument',
            name='privateuploadfilestatus',
        ),
        migrations.RemoveField(
            model_name='privatedocument',
            name='privateuploadfiletransferstatus',
        ),
        migrations.AddField(
            model_name='privatedocument',
            name='upload_file_status',
            field=models.CharField(default='pending', help_text='private_file_status', max_length=300),
        ),
        migrations.AddField(
            model_name='privatedocument',
            name='upload_file_transfer_status',
            field=models.CharField(default='pending', help_text='private_file_transfer_status', max_length=300),
        ),
    ]
