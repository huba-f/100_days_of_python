from django.shortcuts import render
from .forms import AddBook
from .models import Book



# Create your views here.
def home(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'base/index.html', context)


def add(request):
    form = AddBook()
    form_data = AddBook(request.POST or None)
    if form_data.is_valid():
        title = form_data.cleaned_data.get("title")
        author = form_data.cleaned_data.get("author")
        rating = form_data.cleaned_data.get("rating")
        book = Book(title=title, author=author, rating=rating)
        book.save()

    context = {'form': form}
    return render(request, 'base/add.html', context)   