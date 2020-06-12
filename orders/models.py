import random

from django.core.mail import send_mail
from django.db import models
import uuid

# Create your models here.
from BuySellAuto import settings
from aboutus.models import CompanyContactDetails
from businessdirectory.models import Equipment
from store.models import Product


def gen_order_id():
    global unique_order_id
    unique_order_id = 0
    ids = []
    # my_id = uuid.uuid1()
    my_id = random.randint(1, 1000000000)
    unique_order_id = my_id
    # unique_order_id = 124365678
    print('INSIDE GEN_ORDER FUNCT TEST: ', unique_order_id)

    for u_ids in EquipmentOrder.objects.all():
        ids.append(u_ids.order_id)
    # print('PRINTING IDs: ', ids)

    if unique_order_id not in ids:
        print('ORDER ID ALREADY TAKEN: ', unique_order_id)
        return unique_order_id
    else:
        gen_order_id()


class Order(models.Model):
    STATUS_CHOICES = (
        ('Started', 'Started'),
        ('Cancelled', 'Cancelled'),
        ('Finished', 'Finished'),
    )
    id = models.AutoField(primary_key=True, editable=False)
    order_id = models.IntegerField(default=0)
    sub_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    vehicle_of_interest = models.ForeignKey(Product, help_text='Do not change this field', default='',
                                               on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='Started', choices=STATUS_CHOICES)
    cancellation_reason = models.TextField('Cancellation Reason', blank=True, null=False,
                                           help_text='Only use if order cancelled')
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
        return self.contact_name + ' Order: ' + str(self.order_id)

    def save(self, **kwargs):
        global cell, tell, email1, email2, location
        for detail in CompanyContactDetails.objects.all():
            cell = detail.mobile
            tell = detail.telephone
            email1 = detail.emailaddress1
            email2 = detail.emailaddress2
            location = detail.location

        if not self.id:
            print('INSIDE SAVE TEST: ', gen_order_id())
            r_id = gen_order_id()
            self.order_id = r_id

            # send email to admin of new account created
            subject = 'Order %s Successful!' % self.order_id
            message = 'Dear %s, ' \
                      '\nThank you for shopping with us, your order number is %s. ' \
                      'We will now begin processing your order. ' \
                      'We will send you a confirmation email when your item is shipped.' \
                      '\n' \
                      '\n*ORDER DETAILS*' \
                      '\nItem: %s' \
                      '\nPrice: %s' \
                      '\n' \
                      '\n*SHIPPING ADDRESS*' \
                      '\n%s' \
                      '\n' \
                      '\nOUR CONTACTS:' \
                      '\n' \
                      '\nMobile: %s' \
                      '\nTelephone: %s' \
                      '\nEmail 1: %s' \
                      '\nEmail 2: %s' \
                      '\nLocation: %s' \
                      '\nSite: www.buysellauto.com' \
                      % (
                          self.contact_name, self.order_id, self.vehicle_of_interest.title,
                          self.vehicle_of_interest.price,
                          self.city + ', ' + self.street_address, cell, tell, email1, email2, location)
            from_email = 'noreply@buysellauto.com'
            send_mail(subject, message, from_email, recipient_list=[self.email, ],
                      fail_silently=True)

            super(Order, self).save()


        elif self.id:
            if self.status == "Finished":
                print('INSIDE FINISHED TEST: ')

                # send email to admin of new account created
                subject = 'Order %s Successfully Processed!' % self.order_id
                message = 'Dear %s, ' \
                          '\nThank you for shopping with us, your order number is %s. ' \
                          'Has been Shipped!' \
                          '\n' \
                          '\n*ORDER DETAILS*' \
                          '\nItem: %s' \
                          '\nPrice: %s' \
                          '\n' \
                          '\n*SHIPPING ADDRESS*' \
                          '\n%s' \
                          '\n' \
                          '\nOUR CONTACTS:' \
                          '\n' \
                          '\nMobile: %s' \
                          '\nTelephone: %s' \
                          '\nEmail 1: %s' \
                          '\nEmail 2: %s' \
                          '\nLocation: %s' \
                          '\nSite: www.buysellauto.com' \
                          % (self.contact_name, self.order_id, self.vehicle_of_interest.title,
                             self.vehicle_of_interest.price, self.city + ', ' + self.street_address, cell, tell, email1,
                             email2, location)
                from_email = 'noreply@buysellauto.com'
                send_mail(subject, message, from_email, recipient_list=[self.email, ],
                          fail_silently=True)

                super(Order, self).save()

            if self.status == "Cancelled":
                print('INSIDE CANCELLED TEST: ')

                # send email to admin of new account created
                subject = 'Order %s Was Cancelled!' % self.order_id
                message = 'Dear %s, ' \
                          '\nYour order number is %s. ' \
                          'Has been Cancelled with the reason below!' \
                          '\n' \
                          '\n*CANCELLATION REASON*' \
                          '\n%s' \
                          '\n' \
                          '\nOUR CONTACTS:' \
                          '\n' \
                          '\nMobile: %s' \
                          '\nTelephone: %s' \
                          '\nEmail 1: %s' \
                          '\nEmail 2: %s' \
                          '\nLocation: %s' \
                          '\nSite: www.buysellauto.com' \
                          % (self.contact_name, self.order_id, self.cancellation_reason, cell, tell, email1,
                             email2, location)
                from_email = 'noreply@buysellauto.com'
                send_mail(subject, message, from_email, recipient_list=[self.email, ],
                          fail_silently=True)

                super(Order, self).save()


class EquipmentOrder(models.Model):
    STATUS_CHOICES = (
        ('Started', 'Started'),
        ('Cancelled', 'Cancelled'),
        ('Finished', 'Finished'),
    )
    id = models.AutoField(primary_key=True, editable=False)
    order_id = models.IntegerField(default=0)
    sub_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    equipment_of_interest = models.ForeignKey(Equipment, help_text='Do not change this field', default='',
                                            on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='Started', choices=STATUS_CHOICES)
    cancellation_reason = models.TextField('Cancellation Reason', blank=True, null=False,
                                           help_text='Only use if order cancelled')
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
        return self.contact_name + ' Order: ' + str(self.order_id)

    def save(self, **kwargs):
        global cell, tell, email1, email2, location
        for detail in CompanyContactDetails.objects.all():
            cell = detail.mobile
            tell = detail.telephone
            email1 = detail.emailaddress1
            email2 = detail.emailaddress2
            location = detail.location

        if not self.id:
            print('INSIDE SAVE TEST: ', gen_order_id())
            r_id = gen_order_id()
            self.order_id = r_id

            # send email to admin of new account created
            subject = 'Order %s Successful!' % self.order_id
            message = 'Dear %s, ' \
                      '\nThank you for shopping with us, your order number is %s. ' \
                      'We will now begin processing your order. ' \
                      'We will send you a confirmation email when your item is shipped.' \
                      '\n' \
                      '\n*ORDER DETAILS*' \
                      '\nItem: %s' \
                      '\nPrice: %s' \
                      '\n' \
                      '\n*SHIPPING ADDRESS*' \
                      '\n%s' \
                      '\n' \
                      '\nOUR CONTACTS:' \
                      '\n' \
                      '\nMobile: %s' \
                      '\nTelephone: %s' \
                      '\nEmail 1: %s' \
                      '\nEmail 2: %s' \
                      '\nLocation: %s' \
                      '\nSite: www.buysellauto.com' \
                      % (
                          self.contact_name, self.order_id, self.equipment_of_interest.equipment_name,
                          self.equipment_of_interest.equipment_price,
                          self.city + ', ' + self.street_address, cell, tell, email1, email2, location)
            from_email = 'noreply@buysellauto.com'
            send_mail(subject, message, from_email, recipient_list=[self.email, ],
                      fail_silently=True)

            super(EquipmentOrder, self).save()

        elif self.id:
            if self.status == "Finished":
                print('INSIDE FINISHED TEST: ')

                # send email to admin of new account created
                subject = 'Order %s Successfully Processed!' % self.order_id
                message = 'Dear %s, ' \
                          '\nThank you for shopping with us, your order number is %s. ' \
                          'Has been Shipped!' \
                          '\n' \
                          '\n*ORDER DETAILS*' \
                          '\nItem: %s' \
                          '\nPrice: %s' \
                          '\n' \
                          '\n*SHIPPING ADDRESS*' \
                          '\n%s' \
                          '\n' \
                          '\nOUR CONTACTS:' \
                          '\n' \
                          '\nMobile: %s' \
                          '\nTelephone: %s' \
                          '\nEmail 1: %s' \
                          '\nEmail 2: %s' \
                          '\nLocation: %s' \
                          '\nSite: www.buysellauto.com' \
                          % (self.contact_name, self.order_id, self.equipment_of_interest.equipment_name,
                             self.equipment_of_interest.equipment_price, self.city + ', ' + self.street_address, cell, tell, email1,
                             email2, location)
                from_email = 'noreply@buysellauto.com'
                send_mail(subject, message, from_email, recipient_list=[self.email, ],
                          fail_silently=True)

                super(EquipmentOrder, self).save()

            if self.status == "Cancelled":
                print('INSIDE CANCELLED TEST: ')

                # send email to admin of new account created
                subject = 'Order %s Was Cancelled!' % self.order_id
                message = 'Dear %s, ' \
                          '\nYour order number is %s. ' \
                          'Has been Cancelled with the reason below!' \
                          '\n' \
                          '\n*CANCELLATION REASON*' \
                          '\n%s' \
                          '\n' \
                          '\nOUR CONTACTS:' \
                          '\n' \
                          '\nMobile: %s' \
                          '\nTelephone: %s' \
                          '\nEmail 1: %s' \
                          '\nEmail 2: %s' \
                          '\nLocation: %s' \
                          '\nSite: www.buysellauto.com' \
                          % (self.contact_name, self.order_id, self.cancellation_reason, cell, tell, email1,
                             email2, location)
                from_email = 'noreply@buysellauto.com'
                send_mail(subject, message, from_email, recipient_list=[self.email, ],
                          fail_silently=True)

                super(EquipmentOrder, self).save()
