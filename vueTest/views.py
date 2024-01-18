from django.shortcuts import render


def HomePage(request):
    content = dict()

    return render(request, "vueTest/home.html", content)
