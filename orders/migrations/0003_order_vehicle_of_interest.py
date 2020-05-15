# Generated by Django 2.2 on 2020-04-14 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20200414_0517'),
        ('orders', '0002_auto_20200414_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='vehicle_of_interest',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='store.Product'),
        ),
    ]
