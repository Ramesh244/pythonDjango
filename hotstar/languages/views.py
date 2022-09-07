from django.shortcuts import render

# Create your views here.
def telugu(request):
    movie = 'action'
    duration = '2.51 hours'
    subtitles = 'english'
    movie_details = {'mo':movie, 'du':duration, 'su':subtitles}
    return render(request, 'telugu.html', movie_details)

def hindi(request):
    movie = 'action'
    duration = '2.51 hours'
    subtitles = 'hindi'
    movie_details = {'mo':movie, 'du':duration, 'su':subtitles}
    return render(request, 'hindi.html', movie_details)

def english(request):
    movie = 'action'
    duration = '2.51 hours'
    subtitles = 'telugu'
    movie_details = {'mo':movie, 'du':duration, 'su':subtitles}
    return render(request, 'english.html', movie_details)

def tamil(request):
    movie = 'action'
    duration = '2.51 hours'
    subtitles = 'tamil'
    movie_details = {'mo':movie, 'du':duration, 'su':subtitles}
    return render(request, 'tamil.html', movie_details)

def kannada(request):
    movie = 'action'
    duration = '2.51 hours'
    subtitles = 'kannada'
    movie_details = {'mo':movie, 'du':duration, 'su':subtitles}
    return render(request, 'kannada.html', movie_details)