from django.shortcuts import render


def contacts(request):
    """Контролер страницы contacts.html"""
    return render(request, 'catalog/contacts.html')

def home(request):
    """Контролер страницы home.html"""
    return render(request, 'catalog/home.html')
