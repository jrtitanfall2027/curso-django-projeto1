#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Reginaldo Jr',
    })


#def contato(request):
#    return HttpResponse('contato')


#def sobre(request):
#    return HttpResponse('sobre')