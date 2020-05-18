from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from businessdirectory.models import AutoShopAndCarWash, EquipmentType, Equipment, EquipmentImage


class EquipmentTypeAdmin(ImportExportModelAdmin):
    list_display = ('equipment_type', )
    list_display_links = ('equipment_type', )
    list_per_page = 10
    search_fields = ('equipment_type', )


class EquipmentAdmin(ImportExportModelAdmin):
    list_display = ('user', 'equipment_type', 'equipment_name', 'equipment_name',)
    list_display_links = ('user', 'equipment_type', 'equipment_name', )
    list_per_page = 10
    search_fields = ('equipment_type', 'equipment_name', )
    autocomplete_fields = ('equipment_type', 'user')


class EquipmentImageAdmin(ImportExportModelAdmin):
    list_display = ('equipment', 'image', 'featured', 'thumbnail', 'active', 'updated_at')
    list_filter = ('updated_at', 'featured', 'thumbnail', 'active',)
    list_per_page = 10
    autocomplete_fields = ('equipment',)
    date_hierarchy = 'updated_at'


class AutoShopAndCarWashAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'location', 'coordinates', 'contact', 'coverpic', 'profilepic')
    list_display_links = ('name', 'category', 'location', 'coordinates', 'contact', 'coverpic', 'profilepic')
    list_per_page = 10
    search_fields = ('name', 'category', 'location', 'coordinates', 'contact',)



admin.site.register(AutoShopAndCarWash, AutoShopAndCarWashAdmin)
admin.site.register(EquipmentImage, EquipmentImageAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(Equipment, EquipmentAdmin)