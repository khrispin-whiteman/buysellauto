from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

from store.models import Product, Category, ProductImage, ProductVariation, Location, EventType, Event


# Register your models here.
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('category_name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name', 'created_at')
    list_per_page = 10


class ProductAdmin(ImportExportModelAdmin):
    list_display = ('title', 'active', 'price', 'sale_price', 'slug', 'location', 'mileage', 'listing_type', 'category', 'created_at', 'updated_at')
    list_editable = ('price', 'sale_price',)
    search_fields = ('title', 'price', 'category__name')
    list_filter = ('active', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    autocomplete_fields = ('category', )
    date_hierarchy = 'updated_at'


class ProductImageAdmin(ImportExportModelAdmin):
    list_display = ('product', 'image', 'featured', 'thumbnail', 'active', 'updated_at')
    list_filter = ('updated_at', 'featured', 'thumbnail', 'active',)
    list_per_page = 10
    autocomplete_fields = ('product',)
    date_hierarchy = 'updated_at'


class ProductVariationAdmin(ImportExportModelAdmin):
    list_display = ('product', 'title', 'category', 'image', 'price', 'active', 'updated_at')
    list_filter = ('price', 'active',)
    list_per_page = 10
    date_hierarchy = 'updated_at'
    search_fields = ('product', 'title', 'category', 'price',)

class LocationAdmin(ImportExportModelAdmin):
    list_display = ('location_name', )
    list_display_links = ('location_name',)
    search_fields = ('location_name',)
    list_per_page = 10


class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ('event_type_name', 'slug')
    list_display_links = ('event_type_name', 'slug')
    search_fields = ('event_type_name', 'slug')
    prepopulated_fields = {'slug': ('event_type_name',)}
    list_per_page = 10


class EventAdmin(ImportExportModelAdmin):
    list_display = ('event_type', 'event_name', 'slug', 'event_date',)
    list_filter = ('event_type', 'event_date',)
    search_fields = ('event_type', 'event_name', 'slug')
    list_per_page = 10
    prepopulated_fields = {'slug': ('event_name',)}
    autocomplete_fields = ('event_type', )
    date_hierarchy = 'event_date'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
