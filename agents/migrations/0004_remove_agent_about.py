# Generated by Django 2.2 on 2020-04-12 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_agent_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='about',
        ),
    ]
