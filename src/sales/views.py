import pandas as pd

from django.shortcuts import render
from django.views import generic

from .models import Sale
from .forms import SalesSearchForm


def home_view(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None

    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        chart_type = request.POST['chart_type']

        qs = Sale.objects.filter(created__date__gte=date_from,
                                 created__date__lte=date_to)
        if len(qs) > 0:
            sales_df = pd.DataFrame(qs.values())
            sales_df_html = sales_df.to_html()
        else:
            pass
    context = {
        'form': form,
        'sales_df': sales_df_html,
    }
    return render(request, 'sales/home.html', context)


class SaleListView(generic.ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales'


class SaleDetailView(generic.DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
