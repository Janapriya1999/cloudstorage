# Generated by Django 4.1.1 on 2022-11-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0028_privatedocument_random_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatedocument',
            name='random_id',
            field=models.CharField(help_text='random_id', max_length=26, null=True),
        ),
    ]
