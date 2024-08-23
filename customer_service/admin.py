from django.contrib import admin
from .models import Customer, ServiceRequest


admin.site.register(Customer)
admin.site.register(ServiceRequest)