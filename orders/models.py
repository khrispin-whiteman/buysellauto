from django.core.mail import send_mail
from django.db import models

# Create your models here.
from BuySellAuto import settings
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('Started', 'Started'),
        ('Abandoned', 'Abandoned'),
        ('Finished', 'Finished'),
    )
    id = models.AutoField(primary_key=True, editable=False)
    sub_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    vehicle_of_interest = models.OneToOneField(Product, help_text='Do not change this field', default='',
                                               on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='Started', choices=STATUS_CHOICES)
    contact_name = models.CharField('Contact Name (Full Name)', max_length=200, null=False,
                                    help_text='This field is required')
    country_region = models.CharField('Country/Region', max_length=200, null=False, help_text='This field is required')
    province = models.CharField('Province', default='', max_length=200)
    city = models.CharField('City', max_length=200)
    street_address = models.TextField('Street Address', max_length=200, null=False, help_text='This field is required')
    # zip_postal_code = models.CharField('Zip Code', max_length=200, default='')
    phone_number = models.CharField('Phone Number', max_length=200, help_text='This field is required')
    email = models.EmailField('Email', default='', max_length=200, help_text='This field is required')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name + ' Order: ' + str(self.id)

    def save(self, **kwargs):
        if not self.id:
            # send email to admin of new account created
            subject = 'Order %s Successful!' % self.id
            message = 'Dear %s, ' \
                      '\nThank you for shopping with us, your order number %s. ' \
                      'We will now begin processing your order. ' \
                      'We will send you a confirmation email when your item is shipped.' \
                      '\n' \
                      '\n*ORDER DETAILS*' \
                      '\nItem: %s' \
                      '\nPrice: %s' \
                      '\n' \
                      '\n*SHIPPING ADDRESS*' \
                      '\n%s' \
                      % (self.contact_name, self.id, self.vehicle_of_interest.title, self.vehicle_of_interest.price, self.city +', ' + self.street_address)
            from_email = 'Buysellauto.com'
            send_mail(subject, message, from_email, recipient_list=[self.email, ],
                      fail_silently=True)

            super(Order, self).save()
