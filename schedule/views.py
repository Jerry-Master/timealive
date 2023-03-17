from django.http import HttpResponse
from django import template
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    t = template.loader.get_template('schedule.html')
    html = t.render({
        'is_home': False,
        'is_viz': False,
        'is_schedule': True,
    })
    return HttpResponse(html)