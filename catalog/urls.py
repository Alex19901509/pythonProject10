from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    #path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name='catalog_list'),
    path('products/<int:pk>/', products_detail, name='catalog_detail')
]
