from django.contrib import admin

# Register your models here.
# myapp/admin.py
from django.contrib import admin
from .models import Category, Supplier, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'contact_person', 'contact_email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock_quantity', 'category', 'supplier')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'customer_name', 'total_amount')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price')
