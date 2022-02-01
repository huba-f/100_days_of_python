from django.shortcuts import render
from .models import AddBook
from .forms import AddBookForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST or None)
        if form.is_valid():
            form.save()
        all_books = AddBook.objects.all()
        return render(request, 'website/index.html', {'all_books': all_books})
    all_books = AddBook.objects.all()
    return render(request, 'website/index.html', {'all_books': all_books})
    