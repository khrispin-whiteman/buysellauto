from django.urls import path

from orders import views

urlpatterns = [
    path('order_request/', views.OrderRequestView.as_view(), name='order_request'),
    path('order_request/e/', views.EquipmentOrderRequestView.as_view(), name='equipment_order_request'),
    path('order_request_done/', views.order_request_done, name='order_request_done'),
]