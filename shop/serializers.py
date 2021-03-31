from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from datetime import datetime

from .models import Order, OrderLine, OrderEvent, Invoice, GiftCard, Voucher, Sale

class OrderSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    tracking_client_id = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            'id', 
            'status', 
            'user', 
            'tracking_client_id', 
            'billing_address', 
            'shipping_address', 
            'shipping_method', 
            'shipping_price', 
            'total_net_amount', 
            'undiscounted_amount',
        ]
        read_only_fields = ('id','tracking_client_id',)
    
    def get_tracking_client_id(self,obj):
        pass




class OrderLineSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = [
            'order',
            'variant',
            'quantity',
            'quantity_fulfilled',
        ]



class OrderEventSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    
    class Meta:
        model = OrderEvent
        fields = [
            'date',
            'type',
            'order',
            'user',
        ]


class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'order', 
            'number', 
            'created', 
            'external_url', 
            'invoice_file', 
        ]


class GiftCardSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)    
    class Meta:
        model = GiftCard
        fields = [
            'code', 
            'user', 
            'created', 
            'start_date', 
            'end_date', 
            'last_used_on', 
            'is_active', 
            'initial_balance_amount', 
            'current_balance_amount', 
        ]



class VoucherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = [
            'type',
            'name',
            'code',
            'usage_limit',
            'used',
            'start_date',
            'end_date',
            'apply_once_per_order',
            'apply_once_per_customer',
            'discount_value_type',
            'min_checkout_items_quantity',
        ]


class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'name',
            'type',
            'products',
            'categories',
            'collections',
            'start_date',
            'end_date',            
        ]