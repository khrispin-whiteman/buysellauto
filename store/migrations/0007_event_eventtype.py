# Generated by Django 2.2 on 2020-02-19 07:20

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200212_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type_name', models.CharField(max_length=200, verbose_name='Event Type Name')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('event_description', tinymce.models.HTMLField()),
                ('event_date', models.DateTimeField(verbose_name='Date Of Event')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.EventType')),
            ],
        ),
    ]
