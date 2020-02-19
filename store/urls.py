from django.urls import path

from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicles/for-sale/', views.sale_vehicles, name='for_sale'),
    path('vehicles/for-hire/', views.hire_vehicles, name='for_hire'),
    path('vehicles/classified/', views.classified_vehicles, name='classified'),
    path('searched', views.product_search, name='product_search'),
    path('<slug:category_slug>/', views.index, name='product_list_by_category'),
    path('<int:i_d>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('searched/brand/<str:brand>/<str:keywords>', views.search_filters_brand, name='search_filters_brand'),
]