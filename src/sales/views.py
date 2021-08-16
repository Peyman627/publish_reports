import pandas as pd

from django.shortcuts import render
from django.views import generic

from .models import Sale
from .forms import SalesSearchForm
from .utils import get_customer_form_id, get_salesman_from_id


def home_view(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None
    positions_df = None
    merged_df = None

    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        chart_type = request.POST['chart_type']

        sales_qs = Sale.objects.filter(created__date__gte=date_from,
                                       created__date__lte=date_to)
        if len(sales_qs) > 0:
            sales_df = pd.DataFrame(sales_qs.values())
            sales_df['customer_id'] = sales_df['customer_id'].apply(
                get_customer_form_id)
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(
                get_salesman_from_id)
            sales_df['created'] = sales_df['created'].apply(
                lambda dt: dt.strftime('%Y-%m-%d'))
            sales_df.rename(
                {
                    'customer_id': 'customer',
                    'salesman_id': 'salesman',
                    'id': 'sale_id'
                },
                axis=1,
                inplace=True)
            sales_df_html = sales_df.to_html()

            positions_data = [{
                'position_id': position.id,
                'product': position.product.name,
                'quantity': position.quantity,
                'price': position.price,
                'sale_id': position.get_sale_id(),
            } for sale in sales_qs for position in sale.get_positions()]

            positions_df = pd.DataFrame(positions_data)
            positions_df_html = positions_df.to_html()

            merged_df = pd.merge(sales_df, positions_df, on='sale_id')
            merged_df_html = merged_df.to_html()

        else:
            pass
    context = {
        'form': form,
        'sales_df': sales_df_html,
        'positions_df': positions_df_html,
        'merged_df': merged_df_html
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
