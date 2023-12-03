from django.shortcuts import render
from django.http import HttpResponse
def urj(request):
    diction = {
        'title': 'Main!!',
        'values': ['Hi my little mf)'],
        'obj': ['If you want to know more about me and my project, click the button']
    }
    return render(request, 'old/supra.html', diction)


def mf(request):
    return render(request, 'old/kia.html')

