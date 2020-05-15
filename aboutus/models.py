from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class CompanyContactDetails(models.Model):
    location = models.CharField('Company Location', max_length=1000, null=True, blank=True,)
    mobile = models.CharField('Mobile Phone Number', max_length=200, null=True, blank=True, help_text='(E.g) +260970000000')
    telephone = models.CharField('Telephone Number', max_length=200, null=True, blank=True, help_text='(E.g) +(0121) 121 122')
    emailaddress1 = models.CharField('Email Address1', max_length=200, null=True, blank=True, help_text='(E.g) info@example1.com')
    emailaddress2 = models.CharField('Email Address2', max_length=200, null=True, blank=True, help_text='(E.g) info@example1.com')

    def __str__(self):
        return self.location + ', ' + self.mobile + ', ' + self.telephone

    @classmethod
    def object(cls):
        return cls._default_manager.all().first() # Since only one item

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Company Contact Detail'
        verbose_name_plural = 'Company Contact Details'


class CompanySocialMediaLinks(models.Model):
    facebook = models.URLField('Facebook Page Url', null=True, blank=True)
    twitter = models.URLField('Twitter Page Url', null=True, blank=True)
    instagram = models.URLField('Instagram Page Url', null=True, blank=True)

    def __str__(self):
        return self.facebook

    def save(self, *args, **kwargs):
        if not self.pk and CompanySocialMediaLinks.objects.exists():
        # if you'll not check for self.pk
        # then error will also raised in update of exists model
            raise ValidationError('There can be only 1 entry for each field!!')
        return super(CompanySocialMediaLinks, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Company Social Media Link'
        verbose_name_plural = 'Company Social Media Links'

