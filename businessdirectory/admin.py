from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from businessdirectory.models import AutoShopAndCarWash, EquipmentType, Equipment, EquipmentImage, FillingStation, \
    FillingStationDirectory, FinancialInstitutionDirectory, FinancialInstitution, MotorisedService, AutoEngineering, \
    EarthMoving, Training, Transportation


class EquipmentTypeAdmin(ImportExportModelAdmin):
    list_display = ('equipment_type', 'slug')
    list_display_links = ('equipment_type',)
    list_per_page = 10
    search_fields = ('equipment_type',)
    prepopulated_fields = {'slug': ('equipment_type',)}


class EquipmentAdmin(ImportExportModelAdmin):
    list_display = (
    'user', 'equipment_type', 'equipment_name', 'equipment_price', 'equipment_brand', 'equipment_listing_type',
    'equipment_status')
    list_display_links = ('user', 'equipment_type', 'equipment_name',)
    list_per_page = 10
    search_fields = ('equipment_type__equipment_type', 'equipment_name', 'equipment_price',)
    autocomplete_fields = ('equipment_type', 'user')
    list_filter = ('equipment_listing_type', 'equipment_status')
    prepopulated_fields = {'slug': ('equipment_name',)}


class EquipmentImageAdmin(ImportExportModelAdmin):
    list_display = ('equipment', 'image_tag', 'active', 'image', 'updated_at')
    list_filter = ('updated_at', 'active',)
    list_per_page = 10
    autocomplete_fields = ('equipment',)
    search_fields = ('equipment__equipment_name', 'equipment__equipment_name')
    date_hierarchy = 'updated_at'


class AutoShopAndCarWashAdmin(ImportExportModelAdmin):
    list_display = (
    'name', 'category', 'location', 'coordinates', 'slug', 'contact', 'coverpic_tag', 'coverpic', 'profilepic_tag',
    'profilepic')
    list_display_links = ('name', 'category', 'location', 'coordinates', 'slug', 'contact', 'coverpic', 'profilepic')
    list_per_page = 10
    search_fields = ('name', 'category', 'location', 'coordinates', 'slug', 'contact',)
    prepopulated_fields = {'slug': ('name',)}


class FillingStationDirectoryAdmin(ImportExportModelAdmin):
    list_display = ('filling_station_name', 'slug')
    list_display_links = ('filling_station_name', 'slug')
    search_fields = ('filling_station_name', 'slug')
    list_per_page = 10
    prepopulated_fields = {'slug': ('filling_station_name',)}


class FillingStationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    autocomplete_fields = ('name', )
    search_fields = ('name__filling_station_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('location',)}


class FinancialInstitutionDirectoryAdmin(ImportExportModelAdmin):
    list_display = ('financial_institution_name', 'slug')
    list_display_links = ('financial_institution_name', 'slug')
    search_fields = ('financial_institution_name', 'slug')
    list_per_page = 10
    prepopulated_fields = {'slug': ('financial_institution_name',)}


class FinancialInstitutionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    autocomplete_fields = ('name', )
    search_fields = ('name__financial_institution_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('location',)}


class MotorizedServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('name',)}


class AutoEngineeringServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('name',)}


class EarthMovingServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('name',)}


class TrainingServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('name',)}


class TransportationServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'slug', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'slug', 'contact', 'website_link',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(AutoShopAndCarWash, AutoShopAndCarWashAdmin)
admin.site.register(EquipmentImage, EquipmentImageAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(FillingStationDirectory, FillingStationDirectoryAdmin)
admin.site.register(FillingStation, FillingStationAdmin)
admin.site.register(FinancialInstitutionDirectory, FinancialInstitutionDirectoryAdmin)
admin.site.register(FinancialInstitution, FinancialInstitutionAdmin)
admin.site.register(MotorisedService, MotorizedServiceAdmin)
admin.site.register(AutoEngineering, AutoEngineeringServiceAdmin)
admin.site.register(EarthMoving, EarthMovingServiceAdmin)
admin.site.register(Training, TrainingServiceAdmin)
admin.site.register(Transportation, TransportationServiceAdmin)
