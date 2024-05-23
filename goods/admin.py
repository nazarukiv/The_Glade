from django.contrib import admin
from goods.models import Categories, Products
# Register your models here.

#admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', ]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount'] #to display fields
    list_editable = ['discount',] #to edit inside table
    search_fields = ['name', 'description'] #to search by
    list_filter = ['quantity', 'category', 'discount'] #filter by
    fields = [    #show the product items by this order
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount', 'quantity')
    ]

