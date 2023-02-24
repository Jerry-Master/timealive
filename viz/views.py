from django.http import HttpResponse
from django import template


def index(request):
    t = template.loader.get_template('viz.html')
    html = t.render({
        'is_home': False,
        'is_viz': True,
        'is_schedule': False,
    })
    return HttpResponse(html)