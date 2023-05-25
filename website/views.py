from django.shortcuts import render, get_object_or_404

from website.models import Entry


def index(request):
    return render(request, 'website/index.html')


def word_details(request, word):
    word = get_object_or_404(Entry, word=word)
    return render(request, 'website/index.html', {'word': word})
