# Generated by Django 2.2 on 2020-03-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_event_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='', max_length=200, verbose_name='Venue'),
        ),
    ]
