from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_land_request, name='create_land_request'),
    path('work/', views.land_request_list, name='land_request_list'),
    path('search/', views.search_land_requests, name='search_land_requests'),
]