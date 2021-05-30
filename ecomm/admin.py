from ecomm.models import Transaction
from django.contrib import admin
from ecomm.views import Product,Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Transaction)