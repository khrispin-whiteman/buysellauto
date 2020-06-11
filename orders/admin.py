from django.contrib import admin
from orders.models import Order, EquipmentOrder


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'contact_name', 'status', 'country_region', 'province', 'city', 'street_address', 'phone_number', 'email', 'created_at', 'updated_at', 'id', 'vehicle_of_interest',)
    list_filter = ('status',)
    list_display_links = ('order_id', 'status', 'created_at', 'updated_at')
    list_per_page = 10
    date_hierarchy = 'created_at'


class EquipmentOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'contact_name', 'status', 'country_region', 'province', 'city', 'street_address', 'phone_number', 'email', 'created_at', 'updated_at', 'id', 'equipment_of_interest',)
    list_filter = ('status',)
    list_display_links = ('order_id', 'status', 'created_at', 'updated_at')
    list_per_page = 10
    date_hierarchy = 'created_at'


admin.site.register(Order, OrderAdmin)
admin.site.register(EquipmentOrder, EquipmentOrderAdmin)