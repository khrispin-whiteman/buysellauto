# Generated by Django 2.2 on 2020-05-21 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businessdirectory', '0019_auto_20200521_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillingStationDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filling_station_name', models.CharField(max_length=200, verbose_name='Filling Station Name')),
            ],
        ),
        migrations.AlterField(
            model_name='fillingstation',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='businessdirectory.FillingStationDirectory', verbose_name='Filling Station Name'),
        ),
        migrations.AlterField(
            model_name='financialinstitutions',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
