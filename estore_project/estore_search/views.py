from django.shortcuts import render
from django.db.models import Q
from estore_app1.models import Product

# Create your views here.


def search_operation(request):
    search_word = None
    value = None
    if 'search_value' in request.GET:
        search_word = request.GET.get('search_value')
        value = Product.objects.filter(Q(name__contains=search_word) | Q(description__contains=search_word))

    return render(request, 'search.html', dict(search_query=search_word, search_value=value))
