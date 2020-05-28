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
    path('filling_stations/', views.filling_stations_list, name='filling_stations_list'),
    path('filling_stations/<int:id>/', views.filling_stations_detail, name='filling_stations_detail'),
    path('financial_institutions/', views.financial_institutions_list, name='financial_institutions_list'),
    path('financial_institutions/<int:id>/', views.financial_institutions_detail, name='financial_institutions_detail'),
    path('motorized_services/', views.motorized_services_list, name='motorized_services_list'),
    path('motorized_services/<int:id>/', views.motorized_service_detail, name='motorized_service_detail'),
    path('auto_engineering_services/', views.auto_engineering_list, name='auto_engineerings_list'),
    path('auto_engineering_services/<int:id>/', views.auto_engineering_detail, name='auto_engineering_detail'),
    path('earth_moving_services/', views.earth_moving_list, name='earth_movings_list'),
    path('earth_moving_services/<int:id>/', views.earth_moving_detail, name='earth_moving_detail'),
    path('training_services/', views.training_services_list, name='training_services_list'),
    path('training_services/<int:id>/', views.training_service_detail, name='training_service_detail'),
    path('transportation_services/', views.transportation_services_list, name='transportation_services_list'),
    path('transportation_services/<int:id>/', views.transportation_service_detail, name='transportation_service_detail'),
]
