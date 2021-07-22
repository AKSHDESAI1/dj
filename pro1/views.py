from django.http import HttpResponse


def a1(request):
    return HttpResponse("<h1>Meshv2 Patel</h1><br><a href='/app2/'>Go to shop</a>")
