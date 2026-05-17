from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, path
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from blog import views
from catalog.forms import ProductForm
from catalog.models import Product, Contact, Feedback, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView ,DeleteView

from catalog.services import get_products_by_category


class ContactsListView(ListView):
    """Отображение списка контактных данных компании"""
    model = Contact
    template_name = 'catalog/contacts.html'
    context_object_name = 'contacts'

class ProductListView(ListView):
    """Отображение списка всех доступных продуктов"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        if settings.CACHE_ENABLED:
            key = 'products_list'
            cache_data = cache.get(key)
            if cache_data is None:
                cache_data = queryset
                cache.set(key, cache_data)
            return cache_data
        return queryset

class ProductDetailView(LoginRequiredMixin, DetailView):
    """Отображение детальной информации об одном конкретном продукте"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание нового продукта через форму на сайте"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        # Автоматически привязываем владельца
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование существующего продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        # Редактировать может владелец или модератор (если есть право на изменение)
        user = self.request.user
        product = self.get_object()
        return user == product.owner or user.has_perm('catalog.can_unpublish_product')

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление продукта с подтверждением"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        # Удалять может владелец или модератор
        user = self.request.user
        product = self.get_object()
        return user == product.owner or user.has_perm('catalog.delete_product')

class CategoryListView(ListView):
    """Отображение списка всех категорий товаров"""
    model = Category
    template_name = 'catalog/categories.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    """Добавление новой категории"""
    model = Category
    fields = ['name', 'description']
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:home')

class CategoryUpdateView(UpdateView):
    """Редактирование существующей категории"""
    model = Category
    fields = ['name', 'description']
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:home')

class CategoryDeleteView(DeleteView):
    """Удаление категории"""
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class FeedbackCreateView(CreateView):
    """
    Контроллер страницы контактов.
    Позволяет пользователю отправить сообщение (сохраняется в Feedback)
    и отображает контактную информацию компании (из Contact).
    """
    model = Feedback
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')

    def get_context_data(self, **kwargs):
        """Здесь мы достаем контакты компании из базы."""
        context = super().get_context_data(**kwargs)
        context['contact_data'] = Contact.objects.all()
        return context

    def form_valid(self, form):
        """Этот метод срабатывает, когда данные в форме верны"""
        response = super().form_valid(form)
        print(f"Сообщение сохранено: {self.object.name}")
        return response

class CategoryProductsListView(ListView):
    """Отображение продуктов конкретной категории с использованием сервисной функции"""
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category_id = self.kwargs.get('pk')
        return get_products_by_category(self.category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.category_id)
        return context