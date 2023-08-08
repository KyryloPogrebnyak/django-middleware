from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

## index view
def index(request):
    return HttpResponse(loader.get_template('pages/home.html').render(context={"pageName": "Landing Page"}))

def add(request):
    word = None
    if request.method == 'POST':
        word = request.POST.get('word')
    return render(request, "pages/add.html", context={"pageName": "Add Something", "word": word})