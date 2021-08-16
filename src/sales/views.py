from django.shortcuts import render


def home_view(request):
    hello = 'hello world from the view'
    return render(request, 'sales/main.html', {'hello': hello})
