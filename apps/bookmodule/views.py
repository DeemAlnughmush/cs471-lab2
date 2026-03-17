from django.shortcuts import render
from django.http import HttpResponse 

def index(request): 
    return render(request, "bookmodule/index.html") 

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')

def index2(request, val1 = 0):   #add the view function (index2) 
    return HttpResponse("value1 = "+str(val1))
