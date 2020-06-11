from django.urls import path

from orders import views

urlpatterns = [
    path('order-request/', views.OrderRequestView.as_view(), name='order_request'),
    path('order-request/e/', views.EquipmentOrderRequestView.as_view(), name='equipment_order_request'),
    path('order-request_done/', views.order_request_done, name='order_request_done'),
    path('equipment-order-request/<int:id>/<slug:slug>/', views.submit_equipment_order, name='submit_equipment_order'),
]