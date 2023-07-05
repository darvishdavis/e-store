from django.shortcuts import render, get_object_or_404, redirect
from estore_app1.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

def split_into_pages(request, elements):
    pages = Paginator(elements, 6)  # contains all pages with 6 products in each page
    try:
        page_no = int(request.GET.get('sheet'))    # user requested page.no
    except:
        page_no = 1

    try:
        products = pages.page(page_no)  # takes the user requested page (with associated product details) from <pages>
    except InvalidPage:
        products = pages.page(pages.num_pages)   # takes last page (with associated product details) from <pages> as <(pages.num_pages)> retrieves integer value of total number of pages.
    return pages, products


def category(request, slug_cat=None):
    ctgry = None
    elements = None
    if slug_cat != None:   # or is not
        ctgry = get_object_or_404(Category, slug=slug_cat )
        elements = Product.objects.all().filter(category=ctgry, available=1)
    else:
        elements = Product.objects.all().filter(available=1)
    a, b = split_into_pages(request, elements)
    return render(request, "categories.html", {'categories': ctgry, 'pages': a, 'products': b})


def product(request, slug_cat=None, slug_prod=None):
    try:
        details = Product.objects.get(category__slug=slug_cat, slug=slug_prod)
    except Exception as e:
        raise e
    return render(request, 'products.html', {'details': details})