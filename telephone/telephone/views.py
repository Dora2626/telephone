from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render


def add_contact(request):
    # return HttpResponse('Hi')
    return render(request, 'telephone/index.html')


def blank_page(request):
    # return HttpResponse('Hi')
    return render(request, 'telephone/blank_page.html')


def main_page(request):
    # return HttpResponse('Hi')
    return render(request, 'telephone/main_page.html')


def say_test(request):
    name = request.POST.get("name")
    fam = request.POST.get("fam")
    context = {"name": name, "fam": fam}
    return render(request, 'telephone/priv.html', context)
