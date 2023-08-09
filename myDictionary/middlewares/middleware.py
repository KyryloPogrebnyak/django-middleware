from django.http import HttpResponse

"""
    #This Middleware to print/store the request info from the client
"""
def requestLoggerMiddleware(getResponse):

    def middleware(req):
        print("\u001b[32mMy first Middleware is working\u001b[0m")
        # print query
        # http://localhost:5000/?car=bmw&color=red
        car = req.GET.get('car') # ===> bmw
        print(car)
        color = req.GET.get('color')
        print(color)
        # to dir/ explor objects in python, use dir(OBJ)
        # print(dir(req.GET))
        # for q in req.GET.items():
        #     print(q)
        response = getResponse(req)
        # some processing, missing some params/ queries
        # return HttpResponse("You are looking for a " + car + " with color: " + color)
        return response
    
    return middleware

def requestLoggerMiddleware2(getResponse):

    def middleware(req):
        print("\u001b[32mMy second Middleware is working\u001b[0m")
        response = getResponse(req)

        return response

    return middleware

def CheckWordEntry(getResponse):

    def middleware(request):
        response = getResponse(request)
        if request.path == "/add/" and request.method == "POST":
            english = request.POST.get("english")
            german = request.POST.get("german")
            if english == "" or german == "":
                return HttpResponse("Please add a word.")
            elif english.isnumeric() or german.isnumeric():
                return HttpResponse("Please enter letters instead of numbers.")
            elif len(english) < 2 or len(german) < 2:
                return HttpResponse("Please add a real word.")
            
        return response
    
    return middleware