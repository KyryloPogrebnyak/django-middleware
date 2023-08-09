from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word, WordForm
# Create your views here.

## index view
def index(request):
    return HttpResponse(loader.get_template('pages/home.html').render(context={"pageName": "Landing Page"}))

def add(request):
    if request.method == 'GET':
        return HttpResponse(loader.get_template("pages/add.html").render(context={"pageName": "Add Word", "form": WordForm()}, request=request))
    else:
        wordForm = WordForm(request.POST)
        if wordForm.is_valid():
            wordForm.save()
            return HttpResponse("Done")
        else:
            return HttpResponse("ERROR, not saved.")
        
def all_words(request):
    words = Word.objects.all()
    return render(request, 'pages/all_words.html', {'pageName': 'All Words', 'words': words})

def search(request):
    search_term = request.GET.get('q', '')
    if search_term:
        words = Word.objects.filter(english__icontains=search_term) | Word.objects.filter(german__icontains=search_term)
    else:
        words = []

    return render(request, 'index.html', {'pageName': 'Search Results', 'search_term': search_term, 'words': words})
