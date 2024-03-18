from django.urls import path
from .views import region_list, create_region, edit_region, delete_region, region_detail

urlpatterns = [
    path('', region_list, name='region_list'),
    path('<int:region_id>/', region_detail, name='region_detail'),
    path('create/', create_region, name='create_region'),
    path('edit/<int:pk>/', edit_region, name='edit_region'),
    path('delete/<int:pk>/', delete_region, name='delete'),
]
