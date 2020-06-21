from django.urls import path

from agents import views

urlpatterns = [
  path('register/', views.AgentRegisterView.as_view(), name='agentregister'),
  path('login/', views.user_login, name='login'),
  path('dashboard/', views.agent_dashboard, name='agentdashboard'),
  path('profile/', views.agent_profile, name='agent_profile'),
  path('profile/update', views.agent_profile_update, name='agent_profile_update'),
  path('agent/vehicles', views.agent_vehicles, name='agent_vehicles'),
  path('agent/vehicles/<int:pk>/', views.agent_vehicle_detail, name='agent_vehicle_detail'),
  path('agent/equipment', views.agent_equipments, name='agent_equipments'),
  path('agent/equipment/<int:pk>/', views.agent_equipment_detail, name='agent_equipment_detail'),
  path('agents/', views.agents_list, name='agents_list'),
  path('agents/details/<int:pk>/', views.agents_details, name='agents_details'),
]