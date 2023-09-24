from django.contrib import admin

from app.models import Kasvattaja, Lemmikki

@admin.register(Lemmikki)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Kasvattaja)
class SupplierAdmin(admin.ModelAdmin):
    pass
