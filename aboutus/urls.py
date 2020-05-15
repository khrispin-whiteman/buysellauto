from django.urls import path

from aboutus import views

urlpatterns = [
    path('contactus/', views.contactus, name='contactus'),
]