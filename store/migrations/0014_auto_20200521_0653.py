# Generated by Django 2.2 on 2020-05-21 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20200425_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='thumbnail',
        ),
    ]
