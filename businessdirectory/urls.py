from django.urls import path

from businessdirectory import views

urlpatterns = [
    path('equipments/', views.equipments, name='equipments'),
    path('equipments/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('car_wash/', views.car_wash_view, name='car_wash_view'),
    path('car_wash/<int:id>/', views.car_wash_detail, name='car_wash_detail'),
    path('auto_shop/', views.auto_shop_view, name='auto_shop_view'),
    path('auto_shop/<int:id>/', views.auto_shop_detail, name='auto_shop_detail'),
    path('sendmail/', views.send_mail, name='sendmail'),
]
