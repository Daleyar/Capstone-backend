from django.contrib import admin
from .models import Products
from .models import Reviews
from .models import Category
from .models import ShoppingCart

admin.site.register(Products)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(ShoppingCart)