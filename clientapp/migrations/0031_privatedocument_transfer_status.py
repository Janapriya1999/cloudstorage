# Generated by Django 4.1.1 on 2022-11-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0030_alter_privatedocument_random_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatedocument',
            name='transfer_status',
            field=models.CharField(default='not-transfer', help_text='transfer_status', max_length=300),
        ),
    ]
