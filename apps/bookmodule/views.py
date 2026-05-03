from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book
from django.db.models import Q 
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student

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

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html') 

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True

            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    
    return render(request, 'bookmodule/search.html')

def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3]

def add_book(request):
    # mybook = 
    Book.objects.create(
        title='Continuous Delivery',
        author='J.Humble and D. Farley',
        edition=1
    )
    # mybook.save() 

    return HttpResponse("Book Added Successfully")

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='the')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1: 
        return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else: 
        return render(request, 'bookmodule/index.html')
    

def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task2(request):
    mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task3(request):
    mybooks = Book.objects.filter(Q(edition__lte=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8task5.html', {'stats': stats})

def lab8_task7(request):
    data = Student.objects.values('address__city').annotate(num_students=Count('id'))
    return render(request, 'bookmodule/lab8task7.html', {'data': data})
