# Generated by Django 2.2 on 2020-04-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessdirectory', '0004_auto_20200412_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoshopandcarwash',
            name='category',
            field=models.CharField(choices=[('Car Wash', 'Car Wash'), ('Auto Shop', 'Auto Shop')], max_length=200, verbose_name='Category'),
        ),
    ]
