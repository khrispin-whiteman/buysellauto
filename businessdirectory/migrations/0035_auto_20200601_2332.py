# Generated by Django 2.2 on 2020-06-01 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessdirectory', '0034_auto_20200601_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fillingstation',
            options={'verbose_name_plural': 'Filling Stations Locations'},
        ),
        migrations.AlterModelOptions(
            name='fillingstationdirectory',
            options={'verbose_name_plural': 'Filling Stations Directory/Names'},
        ),
    ]
