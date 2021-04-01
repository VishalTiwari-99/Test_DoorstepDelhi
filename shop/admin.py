from django.contrib import admin
import nested_admin

from .models import Order, OrderLine, OrderEvent, Invoice, GiftCard, Voucher, Sale

class OrderLineAdmin(nested_admin.NestedStackedInline):
    model = OrderLine

class InvoiceAdmin(nested_admin.NestedStackedInline):
    model = Invoice

class OrderEventAdmin(nested_admin.NestedStackedInline):
    model = OrderEvent

class OrderAdmin(nested_admin.NestedModelAdmin):
    inline = [OrderLineAdmin, InvoiceAdmin, OrderEventAdmin,]


admin.site.register(Voucher)
admin.site.register(GiftCard)
admin.site.register(OrderEvent)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sale)