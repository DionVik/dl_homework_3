# Generated by Django 4.1.3 on 2022-12-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0010_remove_advertisment_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='region',
            field=models.CharField(max_length=35),
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
