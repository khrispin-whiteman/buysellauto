# Generated by Django 2.2 on 2020-04-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessdirectory', '0009_equipment_equipment_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoshopandcarwash',
            name='is_autoshopandcarwash_model',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='is_equipment_model',
            field=models.BooleanField(default=True),
        ),
    ]
