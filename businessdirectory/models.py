from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
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
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equipment.equipment_name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 50px; height: 50px;"/>' % self.image.url)
        else:
            return 'No image found!'
    image_tag.short_description = 'Image'


# class AutoEngineering(models.Model):
# class AutoEngineering(models.Model):

# Auto shops/Car was/etc
class AutoShopAndCarWash(models.Model):
    is_autoshopandcarwash_model = models.BooleanField(default=True, editable=False)
    category = models.CharField('Category', choices=AUTOSHOPANDCARWASH, max_length=200)
    name = models.CharField('Name', max_length=200, help_text='name of car wash')
    location = models.CharField('Location', max_length=200, help_text='location of car wash')
    contact = models.CharField('Contact Details', max_length=200, help_text='cell/tell/fax')
    description = HTMLField(help_text='Services offered...')
    coverpic = models.ImageField(upload_to='carwash/coverpic/%Y/%m/%d', null=True, blank=True)
    profilepic = models.ImageField(upload_to='carwash/profilepic/%Y/%m/%d', null=True, blank=True)
    facebook_link = models.URLField(default='www.facebook.com')
    twitter_link = models.URLField(default='www.twitter.com')
    instagram_link = models.URLField(default='www.instagram.com')
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='', help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    website_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Auto shops/Car wash/etc'
        verbose_name = 'Auto shops/Car wash/etc'

    def coverpic_tag(self):
        if self.coverpic:
            return mark_safe('<img src="%s" style="width: 50px; height: 50px;"/>' % self.coverpic.url)
        else:
            return 'No image found!'
    coverpic_tag.short_description = 'Cover Pic'

    def profilepic_tag(self):
        if self.profilepic:
            return mark_safe('<img src="%s" style="width: 50px; height: 50px;"/>' % self.profilepic.url)
        else:
            return 'No image found!'
    profilepic_tag.short_description = 'Profile Pic'

# done
class FillingStationDirectory(models.Model):
    filling_station_name = models.CharField('Filling Station Name', max_length=200)

    def __str__(self):
        return self.filling_station_name


class FillingStation(models.Model):
    name = models.ForeignKey(FillingStationDirectory, verbose_name="Filling Station Name", on_delete=models.CASCADE)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    website_link = models.URLField(null=True, blank=True, help_text='Optional')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def picture_tag(self):
        if self.picture:
            return mark_safe('<img src="%s" style="width: 50px; height: 50px;"/>' % self.picture.url)
        else:
            return 'No image found!'
    picture_tag.short_description = 'Image'


class FinancialInstitutions(models.Model):
    name = models.CharField('Name', max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='financialinstitution/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    website_link = models.URLField(null=True, blank=True, help_text='Optional')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class MotorisedServices(models.Model):
    name = models.CharField("name", max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True, help_text='Optional')

    def __str__(self):
        return self.name


class EarthMoving(models.Model):
    name = models.CharField("name", max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True, help_text='Optional')

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField("name", max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True, help_text='Optional')

    def __str__(self):
        return self.name


class AutoEngineering(models.Model):
    name = models.CharField("name", max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True, help_text='Optional')

    def __str__(self):
        return self.name


class Transportation(models.Model):
    name = models.CharField("name", max_length=200)
    location = models.CharField('Location', max_length=200, )
    picture = models.ImageField(upload_to='fillingstation/%Y/%m/%d', null=True, blank=True)
    coordinates = models.CharField('Coordinates', null=True, blank=True, max_length=200, default='',
                                   help_text='Check name of the place on google maps or can use latitude and longitude (lati,longi)')
    contact = models.CharField('Contact', max_length=200, null=True, blank=True)
    website_link = models.URLField(null=True, blank=True, help_text='Optional')

    def __str__(self):
        return self.name