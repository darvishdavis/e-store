from django.shortcuts import render, get_object_or_404

from estore_app1.models import Category, Product


# Create your views here.

# Create your views here.
def home(request):
    return render(request, "home.html" )


def category(request, slug_cat=None):
    page = None
    elements = None
    if slug_cat != None:   # or is not
        page = get_object_or_404(Category, slug=slug_cat )
        elements = Product.objects.all().filter(category=page, available=1)
    else:
        elements = Product.objects.all().filter(available=1)
    return render(request, "categories.html", {'products': elements, 'categories': page,})


def product(request,slug_cat=None, slug_prod=None):
    try:
        details = Product.objects.get(category__slug=slug_cat, slug=slug_prod)
    except Exception as e:
        raise e
    return render(request, 'products.html', {'details': details})