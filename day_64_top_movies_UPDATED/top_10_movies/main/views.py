from django.shortcuts import render, redirect
from .models import AddMovie
from .forms import AddMovieForm


# Create your views here.
def home(request):
    all_movies = AddMovie.objects.all().order_by('-ranking')
    return render(request, 'main/index.html', {'all_movies': all_movies})

def add(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST or None)
        if form.is_valid():
            form.save()
        all_movies = AddMovie.objects.all().order_by('-ranking')
        return render(request, 'main/index.html', {'all_movies': all_movies})    
    else:
        form = AddMovieForm()
    all_movies = AddMovie.objects.all().order_by('-ranking')
    return render(request, 'main/add.html', {'all_movies': all_movies, 'form': form})

def update_movie(request, movie_id):
    movie = AddMovie.objects.get(pk=movie_id)
    form = AddMovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/add.html', {'movie': movie,'form': form})

def delete_movie(request, movie_id):
    movie = AddMovie.objects.get(pk=movie_id)
    movie.delete()
    return redirect('home')