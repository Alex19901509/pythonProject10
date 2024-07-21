from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")

    return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ("name_product", "description", "picture", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy("catalog:catalog_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name_product", "description", "picture", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy("catalog:catalog_list")

    def get_success_url(self):
        return reverse("catalog:catalog_detail", args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog_delete")













