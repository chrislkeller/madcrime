from easy_maps.models import Address
from django.contrib import admin

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'computed_address', 'latitude', 'longitude', 'geocode_error']
    list_filter = ['geocode_error']
    search_fields = ['address']

admin.site.register(Address, AddressAdmin)