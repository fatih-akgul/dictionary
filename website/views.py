from django.shortcuts import render, get_object_or_404, redirect

from website.models import Entry


def index(request):
    return render(request, 'website/index.html')


def word_details(request, word):
    word_obj = get_object_or_404(Entry, word=word)
    return render(request, 'website/index.html', {'word': word_obj})


def lookup_redirect(request):
    word = request.POST.get('word')
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return redirect('website:word_details', word)
