from django.contrib import admin
from django.contrib.auth.models import Group

from aboutus.models import CompanyContactDetails, CompanySocialMediaLinks


# Register your models here.
class CompanyContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('location', 'mobile', 'telephone', 'emailaddress1', 'emailaddress2')
    list_display_links = ('location',)
    list_editable = ('mobile', 'telephone', 'emailaddress1', 'emailaddress2')
    search_fields = ('mobile', 'telephone', 'emailaddress1', 'emailaddress2')
    list_per_page = 1


class CompanySocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'facebook', 'twitter', 'instagram',)
    list_display_links = ('id',)
    list_editable = ('facebook', 'twitter', 'instagram',)
    search_fields = ('facebook', 'twitter', 'instagram',)
    list_per_page = 1


admin.site.register(CompanyContactDetails, CompanyContactDetailsAdmin)
admin.site.register(CompanySocialMediaLinks, CompanySocialMediaLinksAdmin)
admin.site.unregister(Group)