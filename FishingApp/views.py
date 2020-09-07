from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        print(request.POST['login'] + '\n' + request.POST['password'])
        return HttpResponse('Вы попались!<br>' +
                            'Ваш логин: ' + request.POST['login'] +
                            '<br>Ваш пароль: ' + request.POST['password'])
    return render(request, 'index.html')


def first_page(request):
    return render(request, 'first.html')
