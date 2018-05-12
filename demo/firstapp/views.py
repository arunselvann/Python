from django.http import HttpResponse
from django.template import loader
from firstapp.models import Category, Item


def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all()
    }
    return HttpResponse(template.render(context, request))


def item(request, item_id):
    try:
        I = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        I = None
    template = loader.get_template('item.html')
    context = {
        'item': I
    }
    return HttpResponse(template.render(context, request))
