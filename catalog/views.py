from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from catalog.forms import ProductForm
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



def index(request):
    """Главная страница: вывод всех товаров с пагинацией"""
    product_list = Product.objects.all().order_by('-created_at')

    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }
    return render(request, 'catalog/home.html', context)


def show_product(request, pk: int):
    """Страница подробной информации о товаре"""
    product = get_object_or_404(Product, id=pk)
    context = {
        "object": product,
    }
    return render(request, "catalog/product_detail.html", context)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:index')
    else:
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {'form': form})
