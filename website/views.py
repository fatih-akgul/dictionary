from django.urls import reverse
from django.views import generic
from website.models import Entry


class IndexView(generic.TemplateView):
    template_name = 'website/index.html'


class WordView(generic.DetailView):
    model = Entry
    context_object_name = 'word'  # name of the retrieved object in the template
    slug_url_kwarg = 'word'  # name of the lookup parameter in urls.py
    slug_field = 'word'  # name of the field in the model to lookup
    template_name = 'website/index.html'


class LookupRedirectView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'website:word_details'

    def get_redirect_url(self, *args, **kwargs):
        word = self.request.POST.get('word')
        url = reverse(self.pattern_name, args=(word,))
        return url
