from django.urls import path

from businessdirectory import views

urlpatterns = [
    path('equipments/', views.equipments, name='equipments'),
    path('equipments/categories/<slug:category_slug>/', views.equipments, name='equipment_list_by_category'),
    path('equipments/<slug:slug>/', views.equipment_detail, name='equipment_detail'),
    path('car-wash/', views.car_wash_view, name='car_wash_view'),
    path('car-wash/<slug:slug>/', views.car_wash_detail, name='car_wash_detail'),
    path('auto-shop/', views.auto_shop_view, name='auto_shop_view'),
    path('auto-shop/<slug:slug>/', views.auto_shop_detail, name='auto_shop_detail'),
    path('sendmail/', views.send_mail, name='sendmail'),
    path('filling-stations/', views.filling_stations_list, name='filling_stations_list'),
    path('filling-stations/name/<slug:category_slug>/', views.filling_stations_list, name='filling_station_list_by_name'),
    path('filling-stations/<str:name>/<slug:slug>/', views.filling_stations_detail, name='filling_stations_detail'),
    path('financial-institutions/', views.financial_institutions_list, name='financial_institutions_list'),
    path('financial-institutions/name/<slug:category_slug>/', views.filling_stations_list, name='financial_institution_list_by_name'),
    path('financial-institutions/<str:name>/<slug:slug>/', views.financial_institutions_detail, name='financial_institutions_detail'),
    path('motorized-services/', views.motorized_services_list, name='motorized_services_list'),
    path('motorized-services/<slug:slug>/', views.motorized_service_detail, name='motorized_service_detail'),
    path('auto-engineering-services/', views.auto_engineering_list, name='auto_engineerings_list'),
    path('auto-engineering-services/<slug:slug>/', views.auto_engineering_detail, name='auto_engineering_detail'),
    path('earth-moving-services/', views.earth_moving_list, name='earth_movings_list'),
    path('earth-moving-services/<slug:slug>/', views.earth_moving_detail, name='earth_moving_detail'),
    path('training-services/', views.training_services_list, name='training_services_list'),
    path('training-services/<slug:slug>/', views.training_service_detail, name='training_service_detail'),
    path('transportation-services/', views.transportation_services_list, name='transportation_services_list'),
    path('transportation-services/<slug:slug>/', views.transportation_service_detail,
         name='transportation_service_detail'),
]
