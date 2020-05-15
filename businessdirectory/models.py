from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from store.models import User, Category


# Create your models here.
AUTOSHOPANDCARWASH = (
    ('Car Wash', 'Car Wash'),
    ('Auto Shop', 'Auto Shop')
)

EQUIPMENT_LISTING_TYPE = (
    ('For Sale', 'For Sale'),
    ('For Hire', 'For Hire'),
    ('Classified', 'Classified'),
)

EQUIPMENT_STATUS = (
    ('New', 'New'),
    ('Used', 'Used'),
)


class EquipmentType(models.Model):
    equipment_type = models.CharField('Equipment Type', max_length=200)
    # slug = models.SlugField(max_length=150, default='', unique=True, db_index=True)
    # created_at = models.DateTimeField(auto_now_add=True, default='',)
    # updated_at = models.DateTimeField(auto_now=True, default='',)

    def __str__(self):
        return self.equipment_type



class Equipment(models.Model):
    is_equipment_model = models.BooleanField(default=True, editable=False)
    user = models.ForeignKey(User, verbose_name='Agent Name', null=True, default='', on_delete=models.CASCADE)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    equipment_name = models.CharField(max_length=200,)
    equipment_brand = models.CharField(max_length=200, default='')
    equipment_stock = models.IntegerField(null=True, blank=True, default=1)
    equipment_sold = models.IntegerField(null=True, blank=True, default=0)
    equipment_price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    equipment_listing_type = models.CharField(max_length=200, verbose_name='Listing Type', default='', choices=EQUIPMENT_LISTING_TYPE)
    equipment_status = models.CharField(max_length=200, verbose_name='Equipment Status', default='', choices=EQUIPMENT_STATUS)
    equipment_description = HTMLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.equipment_name


class EquipmentImage(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='equipments/images/%Y/%m/%d', null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equipment.equipment_name


# class AutoEngineering(models.Model):
# class AutoEngineering(models.Model):

# Auto shops/Car was/etc
class AutoShopAndCarWash(models.Model):
    is_autoshopandcarwash_model = models.BooleanField(default=True)
    category = models.CharField('Category', choices=AUTOSHOPANDCARWASH, max_length=200)
    name = models.CharField('Name', max_length=200, help_text='name of car wash')
    location = models.CharField('Location', max_length=200, help_text='location of car wash')
    contact = models.CharField('Contact Details', max_length=200, help_text='cell/tell/fax')
    description = HTMLField(help_text='Services offered...')
    coverpic = models.ImageField(upload_to='carwash/coverpic/%Y/%m/%d', null=True, blank=True)
    profilepic = models.ImageField(upload_to='carwash/profilepic/%Y/%m/%d', null=True, blank=True)
    facebook_link = models.URLField(default='')
    twitter_link = models.URLField(default='')
    instagram_link = models.URLField(default='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Auto shops/Car wash/etc'
        verbose_name = 'Auto shops/Car wash/etc'


class FillingStation(models.Model):
    name = models.CharField("name", max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)


class FinancialInstitutions(models.Model):
    name = models.CharField('name', max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='financialinstitution/%Y/%m/%d', null=True, blank=True)



