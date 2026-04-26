from django.http import HttpResponse
from django.shortcuts import render


def contacts(request):
    """Контролер страницы contacts.html с обратной связью"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse (f"Здравствуйте, {name}! Мы с вами свяжемся!")
    return render(request, 'catalog/contacts.html')

def home(request):
    """Контролер страницы home.html"""
    return render(request, 'catalog/home.html')
