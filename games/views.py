from django.http import HttpResponse
from django.template import loader

from games.models import MatchType


def index(request):
    random_match = MatchType.objects.order_by('?').first()
    template = loader.get_template('index.html')
    context = {
        'random_match': random_match,
    }
    return HttpResponse(template.render(context, request))
