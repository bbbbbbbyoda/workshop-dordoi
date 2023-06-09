from django.contrib import admin
from .models import Product, DetailImage, Order, OrderItem, Category, Worker, OurService, Link


class DetailPhotoInline(admin.TabularInline):
    model = DetailImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        DetailPhotoInline
    ]
    list_display = ['id', 'name', 'is_active', 'price']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderItem)
admin.site.register(DetailImage)
admin.site.register(Worker)
admin.site.register(OurService)
admin.site.register(Link)
