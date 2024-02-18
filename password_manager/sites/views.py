from django.shortcuts import render, redirect, get_object_or_404
from .models import Site
from .forms import FormSite


def index(request):
    return render(request, 'sites/list.html', {'sites': Site.objects.all()})


def form(request, idSite=None):
    site = get_object_or_404(Site, id=idSite) if idSite else None
    form = FormSite(request.POST or None, instance=site)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, 'sites/form.html', {'form': form, 'site': site})


def delete(request, idSite):
    get_object_or_404(Site, id=idSite).delete()
    return redirect('index')
