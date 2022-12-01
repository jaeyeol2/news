from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from board.models import News

def list(request):
    posts = News.objects.all()
    # return render(request, "list.html")
    return render(request, 'list.html', {'posts': posts})

# url.py , views.py , settings.py