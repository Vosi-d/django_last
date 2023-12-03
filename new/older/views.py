from django.shortcuts import render, redirect
from .models import Arka
from .forms import ArkaForm
from django.views.generic import DetailView
def new_home(request):
    news = Arka.objects.all()
    return render(request, 'older/lada.html', {'news': news})

class Views(DetailView):
    model = Arka
    template_name = 'older/details_view.html'
    context_object_name = 'art'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'error_macros'


    form = ArkaForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'older/create.html', data)

