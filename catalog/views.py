from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    """Получаем 5 последних товаров и передаем их в шаблон"""
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    context = {
        'products': latest_products
    }
    return render(request, 'catalog/home.html', context)


def show_product(request, pk: int):
    """Страница подробной информации о товаре"""
    product = get_object_or_404(Product, id=pk)
    context = {
        "object": product,
    }
    return render(request, "catalog/product_detail.html", context)
