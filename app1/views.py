from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost99

# Create your views here.
def index(request):
    myposts = Blogpost99.objects.all()

    return render(request, 'app11/index.html', {'myposts':myposts})

def blogpost(request, id1):
    post = Blogpost99.objects.filter(post_id=id1)[0]
    print(post)

    return render(request, 'app11/blogpost1.html', {'post':post})