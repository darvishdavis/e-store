from estore_app1.models import Product
from django.db.models import Q
from .models import SearchBox

def search(request):
    search_word = None
    value = None
    if 'search_value' in request.GET:
        search_word = request.GET.get('search_value')
        word = SearchBox.objects.create(value=search_word)
        word.save()
        value = Product.objects.all().filter(Q(name__contains=word.value) | Q(description__contains=word.value))
    return dict(value=value)