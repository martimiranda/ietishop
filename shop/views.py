from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def product_list(request):
    productes = Producte.objects.all()
    categories = Categoria.objects.all()
    return render(request, "product_list.html",{"productes":productes, "categories":categories}) 

def product_list_category(request, id_cat):
    productes = Producte.objects.filter(categoria=id_cat)
    categoria = Categoria.objects.values_list('nom', flat=True).get(id=id_cat)
    return render(request, "product_list.html",{"productes":productes, "categoria":categoria})

def product_details(request,id_prod):
    producte = Producte.objects.filter(id = id_prod)
    return render(request, "product_details_.html",{"producte":producte})


