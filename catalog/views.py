from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product, Contact


def contacts(request):
    """Контролер страницы contacts.html с обратной связью"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse (f"Здравствуйте, {name}! Мы с вами свяжемся!")
    contact_list = Contact.objects.all()
    return render(request, 'catalog/contacts.html', {'contact_list': contact_list})


def home(request):
    """Контролер страницы home.html"""
    return render(request, 'catalog/home.html')


def index(request):
    """Получаем 5 последних товаров"""
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    for product in latest_products:
        print(f"ID: {product.id}, Название: {product.name}, Цена: {product.price}")

    return render(request, 'catalog/home.html')
