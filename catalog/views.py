from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import render_to_string


# Create your views here.
def catalog(request):
    site_name = "Modern Musician"
    # response_html = "<html><body>Welcome to %s.</body></html>" % site_name
    my_context = {"site_name": site_name}
    # response_html = render_to_string("catalog/sample.html", my_context)
    response_html = render_to_string("catalog.html", my_context)
    return HttpResponse(response_html)
