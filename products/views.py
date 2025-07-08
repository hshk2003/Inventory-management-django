from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item
# Create your views here.


class ItemListView(ListView):
    model = Item
    template_name = 'products/item_list.html'
    context_object_name = 'items'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | Q(sku__icontains=query)
            )
        return qs.order_by('name')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'products/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'sku', 'category', 'supplier', 'quantity', 'price']
    template_name = 'products/item_form.html'
    success_url = reverse_lazy('products:item_list')
    extra_context = {'title': 'Add New Item'}

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'sku', 'category', 'supplier', 'quantity', 'price']
    template_name = 'products/item_form.html'
    success_url = reverse_lazy('products:item_list')
    extra_context = {'title': 'Edit Item'}

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'products/item_confirm_delete.html'
    success_url = reverse_lazy('products:item_list')
    extra_context = {'title':'Confirm Delete'}