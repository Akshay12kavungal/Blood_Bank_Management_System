# donors/urls.py

from django.urls import path
from .views import (
    HomeView,
    DonorListView,
    PatientListView,
    DonorCreateView,
    DonorUpdateView,
    DonorDeleteView,
    DonorDetailView,
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,
    PatientDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('donors/', DonorListView.as_view(), name='donor_list'),
    path('donors/new/', DonorCreateView.as_view(), name='donor_create'),
    path('donors/<int:pk>/', DonorDetailView.as_view(), name='donor_detail'),
    path('donors/<int:pk>/edit/', DonorUpdateView.as_view(), name='donor_update'),
    path('donors/<int:pk>/delete/', DonorDeleteView.as_view(), name='donor_delete'),
    
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/new/', PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
