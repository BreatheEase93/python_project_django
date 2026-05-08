from django.conf import settings
from django.db import models

class Category(models.Model):
    """Класс для категории"""
    name = models.CharField(unique=True, max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.name} '


    class Meta:
        """Порядок сортировки по имени"""
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]



class Product(models.Model):
    """Класс для продуктов"""
    name = models.CharField(max_length=50, unique=True, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to="photos/",verbose_name='Фотография', blank=True, null=True)
    publication = models.BooleanField(default=False, verbose_name='признак публикации')
    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            related_name='products',
            verbose_name='категория'
                                )
    price = models.DecimalField (max_digits=12, decimal_places=2, verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              null=True, blank=True, verbose_name='Владелец')


    def __str__(self):
        return f'{self.name} '

    class Meta:
        """Порядок сортировки по имени"""
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]

class Contact(models.Model):
    """Класс для контактов"""
    name = models.CharField(max_length=100, verbose_name='Имя (Компания)')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Адрес или сообщение', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        """Порядок сортировки по имени"""
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ["name"]

class Feedback(models.Model):
    """Модель для хранения сообщений обратной связи от пользователей"""
    name = models.CharField(max_length=100, verbose_name='Имя (Компания)')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Адрес или сообщение', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        ordering = ('-id',)