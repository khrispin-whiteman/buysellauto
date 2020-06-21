"""BuySellAuto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from store.sitemaps import ProductsSitemap, ProductCategorySitemap, FillingStationsSitemap, \
    FinancialInstitutionDirectorySitemap, FinancialInstitutionsSitemap, EquipmentsSitemap, \
    FillingStationDirectorySitemap, EquipmentCategorySitemap, EventsSitemap, EventtypesSitemap, \
    MotorizedServicesSitemap, AutoEngineeringServicesSitemap, EarthMovingServicesSitemap, TrainingServicesSitemap, \
    TransportationServicesSitemap

sitemaps = {
    'products': ProductsSitemap,
    'product_categories': ProductCategorySitemap,
    'equipments': EquipmentsSitemap,
    'equipment_types': EquipmentCategorySitemap,
    'filling_stations': FillingStationsSitemap,
    'filling_stations_names': FillingStationDirectorySitemap,
    'financial_institutions': FinancialInstitutionsSitemap,
    'financial_institutions_names': FinancialInstitutionDirectorySitemap,
    'events': EventsSitemap,
    'motorized_services': MotorizedServicesSitemap,
    'auto_engineering_services': AutoEngineeringServicesSitemap,
    'earth_moving_services': EarthMovingServicesSitemap,
    'event_types': EventtypesSitemap,
    'traininng_services': TrainingServicesSitemap,
    'transportation_services': TransportationServicesSitemap,
}

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('aboutus.urls')),
    path('', include('agents.urls')),
    path('', include('businessdirectory.urls')),
    path('', include('orders.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('tinymce/', include('tinymce.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', views.LoginView.as_view(), name='login', kwargs={'next_page': '/dashboard/'}),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('accounts/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', views.PasswordChangeDoneView, name='password_change_done'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(template_name='registration/password_reset_view.html'), name='password_reset'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetDoneView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    # path('froala_editor/', include('froala_editor.urls')),
]

admin.site.site_header = 'Buy Sell Auto Administration'
admin.site.index_title = 'System Applications'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
