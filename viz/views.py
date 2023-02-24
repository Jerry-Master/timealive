from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django import template

def index(request):
    t = template.loader.get_template('home.html')
    # c = template.Context({'is_viz': True})
    html = t.render({'is_home': False, 'is_viz': True, 'is_schedule': False})
    return HttpResponse(html)