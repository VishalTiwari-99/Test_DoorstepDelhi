from django.contrib import admin
import nested_admin
from .models import Store, ShippingZone, ShippingMethod
# Register your models here.

class StoreAdmin(nested_admin.NestedModelAdmin):
    model = Store
    extra = 0
    min_num = 1


class ShippingMethodInlineAdmin(nested_admin.NestedStackedInline):
    model = ShippingMethod
    extra = 0
    min_num = 1    


class ShippingZoneAdmin(nested_admin.NestedModelAdmin):
    inline = [ShippingMethodInlineAdmin]
    extra = 0
    min_num = 1

admin.site.register(Store, StoreAdmin)
admin.site.register(ShippingZone, ShippingZoneAdmin)