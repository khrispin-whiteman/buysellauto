from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from businessdirectory.models import AutoShopAndCarWash, EquipmentType, Equipment, EquipmentImage, FillingStation, \
    FillingStationDirectory, FinancialInstitutionDirectory, FinancialInstitution, MotorisedService, AutoEngineering, \
    EarthMoving, Training, Transportation


class EquipmentTypeAdmin(ImportExportModelAdmin):
    list_display = ('equipment_type',)
    list_display_links = ('equipment_type',)
    list_per_page = 10
    search_fields = ('equipment_type',)


class EquipmentAdmin(ImportExportModelAdmin):
    list_display = (
    'user', 'equipment_type', 'equipment_name', 'equipment_price', 'equipment_brand', 'equipment_listing_type',
    'equipment_status')
    list_display_links = ('user', 'equipment_type', 'equipment_name',)
    list_per_page = 10
    search_fields = ('equipment_type__equipment_type', 'equipment_name', 'equipment_price',)
    autocomplete_fields = ('equipment_type', 'user')
    list_filter = ('equipment_listing_type', 'equipment_status')


class EquipmentImageAdmin(ImportExportModelAdmin):
    list_display = ('equipment', 'image_tag', 'active', 'image', 'updated_at')
    list_filter = ('updated_at', 'active',)
    list_per_page = 10
    autocomplete_fields = ('equipment',)
    search_fields = ('equipment__equipment_name', 'equipment__equipment_name')
    date_hierarchy = 'updated_at'


class AutoShopAndCarWashAdmin(ImportExportModelAdmin):
    list_display = (
    'name', 'category', 'location', 'coordinates', 'contact', 'coverpic_tag', 'coverpic', 'profilepic_tag',
    'profilepic')
    list_display_links = ('name', 'category', 'location', 'coordinates', 'contact', 'coverpic', 'profilepic')
    list_per_page = 10
    search_fields = ('name', 'category', 'location', 'coordinates', 'contact',)


class FillingStationDirectoryAdmin(ImportExportModelAdmin):
    list_display = ('filling_station_name',)
    list_display_links = ('filling_station_name',)
    search_fields = ('filling_station_name',)
    list_per_page = 10


class FillingStationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    autocomplete_fields = ('name', )
    search_fields = ('name__filling_station_name', 'location', 'coordinates', 'contact', 'website_link',)


class FinancialInstitutionDirectoryAdmin(ImportExportModelAdmin):
    list_display = ('financial_institution_name',)
    list_display_links = ('financial_institution_name',)
    search_fields = ('financial_institution_name',)
    list_per_page = 10


class FinancialInstitutionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    autocomplete_fields = ('name', )
    search_fields = ('name__financial_institution_name', 'location', 'coordinates', 'contact', 'website_link',)


class MotorizedServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'contact', 'website_link',)


class AutoEngineeringServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'contact', 'website_link',)


class EarthMovingServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'contact', 'website_link',)


class TrainingServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'contact', 'website_link',)


class TransportationServiceAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_display_links = ('name', 'city', 'location', 'coordinates', 'contact', 'website_link', 'picture_tag', 'picture',)
    list_per_page = 10
    search_fields = ('name', 'city__location_name', 'location', 'coordinates', 'contact', 'website_link',)


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
