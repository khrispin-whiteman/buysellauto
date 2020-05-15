from django.urls import path

from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicles/for-sale/', views.sale_vehicles, name='for_sale'),
    path('vehicles/for-hire/', views.hire_vehicles, name='for_hire'),
    path('vehicles/classified/', views.classified_vehicles, name='classified'),
    path('searched/', views.product_search, name='product_search'),
    path('home/<slug:category_slug>/', views.index, name='product_list_by_category'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('<int:i_d>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('order/<int:id>/<slug:slug>/', views.submit_order, name='submit_order'),
    # path('searched/brand/<str:brand>/<str:keywords>/', views.search_filters_brand, name='search_filters_brand'),
    path('all_events/', views.all_events, name='all_events'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('agents/clearing/', views.clearing_agents, name='clearing_agents'),
]