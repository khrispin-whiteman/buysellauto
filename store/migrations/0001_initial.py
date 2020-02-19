# Generated by Django 2.2 on 2020-02-19 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type_name', models.CharField(max_length=200, verbose_name='Event Type Name')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=1000, verbose_name='Name Of Location')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=200, null=True, verbose_name='Brand')),
                ('title', models.CharField(help_text='Name of product', max_length=200, verbose_name='Product Title')),
                ('stock', models.IntegerField(blank=True, default=0, null=True)),
                ('sold', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(default='', max_length=10000, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('listing_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Hire', 'For Hire'), ('Classified', 'Classified')], default='', max_length=200, verbose_name='Listing Type')),
                ('mileage', models.CharField(default=0, max_length=200, verbose_name='Mileage')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.Category')),
                ('location', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='store.Location')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Shop Name')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'unique_together': {('title', 'slug')},
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='products/images/%Y/%m/%d')),
                ('featured', models.BooleanField(default=False)),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='', max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.ProductImage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('event_description', tinymce.models.HTMLField()),
                ('event_date', models.DateTimeField(verbose_name='Date Of Event')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.EventType')),
            ],
        ),
    ]
