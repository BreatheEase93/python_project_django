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
    image = models.ImageField(upload_to="photos/",verbose_name='Фотография')
    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            related_name='products',
            verbose_name='категория'
                                )
    price = models.DecimalField (max_digits=12, decimal_places=2, verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        """Порядок сортировки по имени"""
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
