from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tag)
admin.site.register(Producte)
admin.site.register(Cistella)
admin.site.register(Compra)
admin.site.register(DetallCompra)

class ProducteInline(admin.TabularInline):
    model = Producte
    readonly_fields = ["descripcio"]



class CistellaInline(admin.TabularInline):  
    model = Cistella
    extra = 1 


class CistellaAdmin(admin.ModelAdmin):
    list_display = ('usuari', 'producte', 'quantitat')


class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 0
    exclude = ("descripcio",)

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProducteInline, CategoriaInline]
    list_display = ["nom","parent"]

admin.site.register(Categoria,CategoriaAdmin)
