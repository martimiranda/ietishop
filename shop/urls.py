from django.urls import path,re_path
from . import views, api

urlpatterns = [
    path("", views.product_list),
    path("cat/<id_cat>",views.product_list_category),
    path("<id_prod>",views.product_details),
    path("api/prods",api.getProducts),
    path("api/prods/<int:id_cat>",api.getProductsByCategory),
    path("api/prods/<int:id_cat>/",api.getProductsByCategoryWithLimitation),
    re_path(r'^api/prods/<int:id_cat>/(?P<limit>\d+)/$', api.getProductsByCategoryWithLimitation),
    #path("/cat/<id_cat>"),

]