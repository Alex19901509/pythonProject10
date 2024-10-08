from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path("", ProductListView.as_view(), name='catalog_list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='catalog_detail'),
    path('products/create/', ProductCreateView.as_view(), name='catalog_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='catalog_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='catalog_delete'),
]
