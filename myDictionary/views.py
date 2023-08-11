from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Word, WordForm
# Create your views here.

## index view
def index(request):
    return HttpResponse(loader.get_template('pages/home.html').render(context={"pageName": "Landing Page"}))

def add(req):
    if req.method == "GET":
        return HttpResponse(loader.get_template('pages/add.html').render(context={"pageName": "Add Word", "form": WordForm()}, request=req))
    else:# For POST Request
        # Store the new word
        print("################")
        wordForm = WordForm(req.POST)
        if wordForm.is_valid():
            # Store
            wordForm.save()
            return HttpResponse("Done")
        else:
            return HttpResponse("ERROR, Not saved")
        
def all(req):
    return HttpResponse(loader.get_template('pages/all_words.html').render(context={"pageName": "All Words", "words": Word.objects.all()}, request=req))
        

def search(req):
        q = req.GET.get("q")
        # if exact choise is on
        exact = req.GET.get("exact")
        if exact == "on":
            word = Word.objects.filter(english=q ) or Word.objects.filter(german=q )
            return HttpResponse(loader.get_template('pages/search_results.html').render(context={"pageName": "Search Results", "words": word, "total": len(word)}, request=req)) 
        else:
            # print(req.GET.get("q"))
            # look for word=q, that match in word model/table
            word = Word.objects.filter(english__contains=q ) or Word.objects.filter(german__contains=q )
            # Hint: We can use or own query
            # Word.objects.raw("SELECT * FROM ....")
            # number = Model.objects.filter(column__gte=2) ==> greater than equal 2
            # SELECT * FROM Table WHERE condition1 OR condition2 OR Conditions_n
            # print(dir(word))
            # for w in word:
            #     print(w)
            return HttpResponse(loader.get_template('pages/search_results.html').render(context={"pageName": "Search Results", "words": word, "total": len(word)}, request=req)) 

def delete(request):
    if request.method == "POST":
        print("You ar trying to delete: "+request.POST.get('word_id'))
        word_PK = request.POST.get('word_id')
        Word.objects.filter(pk=word_PK).delete()

        # for i in w:
        #     print(i)
        return HttpResponseRedirect('/all')
    
def edit(request, word_id):
    word = Word.objects.get(pk=word_id)
    if request.method == "GET":
        form = WordForm(instance=word)
        return render(request, 'pages/add.html', context={"pageName": "Edit Word", "form": form})
    else:
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all')
        else:
            return HttpResponse("ERROR, Not saved")
