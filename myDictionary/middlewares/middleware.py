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
        print("\u001b[32mMy CheckWordEntry Middleware is working\u001b[0m")
        
        # Change "add" to "word" to match the form field name
        word = request.POST.get("word")
        
        if word is not None:
            if len(word) < 2:
                print(f"I'm sorry, but the word \'{word}' is too short.\nThe length must be at least two characters.")
            elif word.isnumeric():
                print(f"I'm sorry, but you are able to use only letters. {word} is a number")
            else:
                print(word)
        
        response = getResponse(request)
        return response
    
    return middleware