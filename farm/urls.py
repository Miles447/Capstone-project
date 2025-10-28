from django.urls import path
from . import views

urlpatterns = [
    # Home URL
    path('', views.home, name='home'),

    # Animal URLs
    path('animals/', views.AnimalListView.as_view(), name='animal_list'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('animals/add/', views.AnimalCreateView.as_view(), name='animal_add'),
    path('animals/<int:pk>/edit/', views.AnimalUpdateView.as_view(), name='animal_edit'),
    path('animals/<int:pk>/delete/', views.AnimalDeleteView.as_view(), name='animal_delete'),

    # Produce URLs
    path('produce/', views.ProduceListView.as_view(), name='produce_list'),
    path('produce/<int:pk>/', views.ProduceDetailView.as_view(), name='produce_detail'),
    path('produce/add/', views.ProduceCreateView.as_view(), name='produce_add'),
    path('produce/<int:pk>/edit/', views.ProduceUpdateView.as_view(), name='produce_edit'),
    path('produce/<int:pk>/delete/', views.ProduceDeleteView.as_view(), name='produce_delete'),
]