from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from estore_app1.models import Product
from .models import SearchBox


def split_into_pages(request, elements):
    pages = Paginator(elements, 6)  # contains all pages with 6 products in each page
    try:
        page_no = int(request.GET.get('page', 1))  # user requested page.no
    except:
        page_no = 1

    try:
        products = pages.get_page(page_no)  # takes the user requested page (with associated product details) from <pages>
    except InvalidPage:
        products = pages.get_page(pages.num_pages)  # takes last page (with associated product details) from <pages> as <(pages.num_pages)> retrieves integer value of total number of pages.
    return pages, products


def search_operation(request):
    search_word = None
    value = None
    a, b = None, None
    if 'search_value' in request.GET:
        c = request.method
        search_word = request.GET.get('search_value')
        word = SearchBox.objects.create(value=search_word)
        word.save()
        value = Product.objects.filter(Q(name__contains=word.value) | Q(description__contains=word.value))
        a, b = split_into_pages(request, value)
    else:
        return HttpResponse("not..")
    return render(request, 'search.html', dict(search_query=search_word, pages=a, search_result=value))




