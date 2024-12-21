from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create_property/', views.create_property, name = 'create_property'),
    path('property_details/<str:pk>/', views.property_details, name = 'property_details'),
    path('update_property/<str:pk>/', views.update_property, name = 'update_property'),
    path('delete_property/<str:pk>/', views.delete_property, name = 'delete_property'),

    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),


    path('agents/', views.agents, name = 'agents'),
    path('agent_details/', views.agent_details, name = 'agent_details'),

    path('search/', views.search, name = 'search'),


]
