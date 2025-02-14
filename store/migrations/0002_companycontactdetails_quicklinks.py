# Generated by Django 2.2 on 2020-03-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Location')),
                ('mobile', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mobile Phone Number')),
                ('telephone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telephone Number')),
                ('emailaddress1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email Address')),
                ('emailaddress2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='QuickLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=200, verbose_name='Link Name')),
            ],
        ),
    ]
