# myapp/management/commands/create_initial_data.py
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from decimal import Decimal
from datetime import date
from ProdApp.models import Category, Supplier, Product, Order, OrderItem

class Command(BaseCommand):
    help = 'Populate initial data for the product management system.'

    def handle(self, *args, **options):
        # Create categories
        categories = [
            {'category_name': 'Electronics', 'description': 'Gadgets and electronic devices'},
            {'category_name': 'Clothing', 'description': 'Apparel and fashion items'},
            {'category_name': 'Books', 'description': 'Literary works and publications'},
        ]
        Category.objects.bulk_create(Category(**category_data) for category_data in categories)

        # Create suppliers
        suppliers = [
            {'supplier_name': 'Supplier A', 'contact_person': 'John Doe', 'contact_email': 'john@example.com'},
            {'supplier_name': 'Supplier B', 'contact_person': 'Jane Doe', 'contact_email': 'jane@example.com'},
        ]
        Supplier.objects.bulk_create(Supplier(**supplier_data) for supplier_data in suppliers)

        # Create products
        products = [
            {'product_name': 'Laptop', 'price': Decimal('999.99'), 'stock_quantity': 100, 'category_id': 1, 'supplier_id': 1},
            {'product_name': 'T-shirt', 'price': Decimal('19.99'), 'stock_quantity': 200, 'category_id': 2, 'supplier_id': 2},
            {'product_name': 'Python Book', 'price': Decimal('29.99'), 'stock_quantity': 50, 'category_id': 3, 'supplier_id': 1},
        ]
        Product.objects.bulk_create(Product(**product_data) for product_data in products)

        # Create orders and order items
        order = Order.objects.create(order_date=date.today(), customer_name='John Doe', total_amount=Decimal('0.00'))
        for product in Product.objects.all():
            OrderItem.objects.create(order=order, product=product, quantity=10, unit_price=product.price)

        self.stdout.write(self.style.SUCCESS('Successfully created initial data.'))
