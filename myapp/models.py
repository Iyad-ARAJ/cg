from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.CharField(max_length=255, default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

def get_bookid(id):
    v =Book.objects.get(id=id)
    return v
def get_authorid(id):
    v = Author.objects.get(id=id)
    return v

def all_books():
    return Book.objects.all()

def add_book(title, desc):
    return Book.objects.create(title=title, desc=desc)

def all_authors():
    return Author.objects.all()

def add_author(first_name,last_name,notes):
    return Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)

def add_author_to_book(book_id, author_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    book.authors.add(author)

def add_book_to_author(book_id,author_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)

    author.books.add(book)





