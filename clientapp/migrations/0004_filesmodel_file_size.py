# Generated by Django 4.1.1 on 2022-10-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0003_alter_filesmodel_file_upload_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesmodel',
            name='file_size',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
