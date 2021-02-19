from django.contrib import admin
from .models import PropertyType, Property, PropertyStatus,PropertyCost,SiteVists,Bookings,Notes
# Register your models here.

admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(PropertyStatus)
admin.site.register(PropertyCost)
admin.site.register(SiteVists)
admin.site.register(Bookings)
admin.site.register(Notes)