from django.shortcuts import render
from django.views import generic

from .models import Sale
from .forms import SalesSearchForm


def home_view(request):
    form = SalesSearchForm(request.POST or None)
    context = {'form': form}
    return render(request, 'sales/home.html', context)


class SaleListView(generic.ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'


class SaleDetailView(generic.DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
