from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from .models import Category, Product


# Create your views here.
def catalog(request):
    site_name = "Modern Musician"
    # response_html = "<html><body>Welcome to %s.</body></html>" % site_name
    my_context = {"site_name": site_name}
    # response_html = render_to_string("catalog/sample.html", my_context)
    response_html = render_to_string("catalog.html", my_context)
    return HttpResponse(response_html)


def index(request, template_name="catalog/index.html"):
    page_title = "Musical Instruments and Sheet Music for Musicians"
    return render(
        request,
        template_name,
        locals(),
    )


def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(
        request,
        template_name,
        locals(),
    )


def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(
        request,
        template_name,
        locals(),
    )
