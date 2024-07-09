from django.contrib import admin

from .models import Donor, Patient



# Register your models here.

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'phone_number', 'address', 'availability')
    search_fields = ('name', 'blood_group', 'phone_number', 'address')
    list_filter = ('blood_group', 'availability')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group_needed', 'phone_number', 'address', 'request_date')
    search_fields = ('name', 'blood_group_needed', 'phone_number', 'address')
    list_filter = ('blood_group_needed', 'request_date')