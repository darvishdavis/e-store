from .models import Category, Product


def category_links(request):
    c_link = Category.objects.all()
    p_link = Product.objects.all()
    return dict(c_links=c_link, p_links=p_link)

