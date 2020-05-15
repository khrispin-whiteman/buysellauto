from django.db import models

# Create your models here.
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('Started', 'Started'),
        ('Abandoned', 'Abandoned'),
        ('Finished', 'Finished'),
    )
    #order_id = models.AutoField(unique=True)
    sub_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    vehicle_of_interest = models.OneToOneField(Product, default='', on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='Started', choices=STATUS_CHOICES)
    contact_name = models.CharField('Contact Name (Full Name)', max_length=200, null=False, help_text='This field is required')
    country_region = models.CharField('Country/Region', max_length=200, null=False, help_text='This field is required')
    province = models.CharField('Province', default='', max_length=200)
    city = models.CharField('City', max_length=200)
    street_address = models.TextField('Street Address', max_length=200, null=False, help_text='This field is required')
    #zip_postal_code = models.CharField('Zip Code', max_length=200, default='')
    phone_number = models.CharField('Phone Number', max_length=200, help_text='This field is required')
    email = models.EmailField('Email', default='', max_length=200, help_text='This field is required')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name + ' Order: ' + str(self.id)
