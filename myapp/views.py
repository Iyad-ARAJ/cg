from django.shortcuts import render,redirect
from . import models


def index(request):
    context = {
        'allbooks' : models.all_books(),
    }
    return render(request,'booklist.html',context)

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        models.add_book(title ,desc)
        return redirect('/')

def books(request,id):
    context = {
        'book_info': models.get_bookid(id),
        'authors': models.all_authors()           
    }
    return render(request,'bookinfo.html',context)
  
def add_author_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        models.add_author(first_name, last_name, notes)
        return redirect('add_author')
    else:
        return render(request, 'authorlist.html',{'authors' : models.all_authors() })

def authors(request,id):
    context = {
        'author_info':  models.get_authorid(id),
        'books': models.all_books()           
    }
    return render(request,'authorinfo.html',context)

    
def add_author_to_book_view(request, book_id):
    if request.method == 'POST':
        author_id = request.POST['author_id']
        models.add_author_to_book(book_id, author_id)
        return redirect(f'/books/{book_id}')
    

def add_book_to_author_view(request, author_id):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        models.add_book_to_author(book_id, author_id)
        return redirect(f'/authors/{author_id}')
        



    



    




