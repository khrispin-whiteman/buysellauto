# Generated by Django 2.2 on 2020-05-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessdirectory', '0020_auto_20200521_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillingstation',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AddField(
            model_name='financialinstitutions',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='autoengineering',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='autoengineering',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
        migrations.AlterField(
            model_name='earthmoving',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='earthmoving',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
        migrations.AlterField(
            model_name='fillingstation',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
        migrations.AlterField(
            model_name='financialinstitutions',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
        migrations.AlterField(
            model_name='motorisedservices',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='motorisedservices',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='training',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='contact',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='website_link',
            field=models.URLField(blank=True, help_text='Optional', null=True),
        ),
    ]
