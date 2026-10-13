from django.http import Http404, HttpResponse
from django.shortcuts import render

# Every gift has an unguessable link. Nothing here is listed or searchable.
GIFTS = {
    "toria-8m-k7q2x9": {"template": "gifts/anniversary.html"},
}


def home(request):
    return HttpResponse("NOLAP GIFTS", content_type="text/plain")


def robots(request):
    return HttpResponse("User-agent: *\nDisallow: /g/\n", content_type="text/plain")


def gift(request, slug):
    entry = GIFTS.get(slug)
    if entry is None:
        raise Http404
    response = render(request, entry["template"])
    response["X-Robots-Tag"] = "noindex, nofollow"
    response["Cache-Control"] = "private, max-age=0"
    return response
