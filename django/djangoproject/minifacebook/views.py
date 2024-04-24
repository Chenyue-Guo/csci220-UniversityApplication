from django.shortcuts import render

from .models import Status

@cache_page(60 * 15, cache="special_cache")
def index(request):
    context = {"statuses": Status.objects.order_by('-date_time')[:10]}
    return render(request, "index.html", context)
