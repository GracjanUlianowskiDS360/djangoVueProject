from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from vueTest.models import Worker


def HomePage(request):
    content = dict()

    return render(request, "vueTest/home.html", content)


def create_worker(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Wrong page")

    # w projekcie wykorzystany byłby moduł django Forms do zrobienia walidacji itp., ale nie chce, teraz dodawać pracy
    # ze zmianą inputów
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')

    if not all([name, surname, phone, email]):
        return HttpResponseBadRequest("All fields are required.")

    worker = Worker(name=name, surname=surname, phone=phone, email=email)
    worker.save()

    return redirect('home page')
