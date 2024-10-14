from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<em> First Application Yah</em>")