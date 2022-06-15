from django.shortcuts import render
from django.http.response import HttpResponseRedirect, Http404
from django.views import View
from link_shortener.settings import TIME_ZONE
from .models import Url
from django.views.generic import CreateView

class RedirectToLongUrl(View):
    def get(self, request, short_url):
        try:
            url = Url.objects.get(short_url=short_url)
            if url.valid_until and url.valid_until < TIME_ZONE.now():
                raise Http404('URL is expired')
            return HttpResponseRedirect(url.long_url)
        except Url.DoesNotExist:
            raise Http404('URL does not exist')
        
class UrlCreateView(CreateView):
    model = Url
    fields = ['long_url']
    template_name = 'url/create.html'
    success_url = '/submitted/'
    slug_field = 'short_url'
    slug_url_kwarg = 'short_url'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())