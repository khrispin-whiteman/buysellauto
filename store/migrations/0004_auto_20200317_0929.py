# Generated by Django 2.2 on 2020-03-17 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200317_0847'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyContactDetails',
        ),
        migrations.DeleteModel(
            name='CompanySocialMediaLinks',
        ),
    ]
