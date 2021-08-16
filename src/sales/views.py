from django.shortcuts import render
from django.views import generic

from .models import Sale


def home_view(request):
    hello = 'hello world from the view'
    return render(request, 'sales/home.html', {'hello': hello})


class SaleListView(generic.ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'


class SaleDetailView(generic.DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
