from django.urls import path

from aboutus import views

urlpatterns = [
    path('contactus/', views.contactus, name='contactus'),
    path('legal/', views.legal, name='legal'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy/', views.privacy, name='privacy'),
    path('security/', views.security, name='security'),
    path('payment-methods/', views.payment_methods, name='payment_methods'),
    path('feedback/', views.feedback, name='feedback'),
]