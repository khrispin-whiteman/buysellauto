# Generated by Django 2.2 on 2020-06-10 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_equipmentorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentorder',
            name='vehicle_of_interest',
            field=models.ForeignKey(default='', help_text='Do not change this field', on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]
