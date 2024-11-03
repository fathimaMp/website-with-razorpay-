from django.contrib import admin
from django.urls import reverse
from . models import Product,Customer,Cart,Payment,OrderPlaced,Wishlist
from django.contrib.auth.models import Group
from django.utils.html import format_html

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','mobile','state','zipcode']

@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razor_payment_id','paid']
    

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status','payment']


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']
        

