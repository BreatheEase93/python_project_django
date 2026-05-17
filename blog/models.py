from django.db import models

class Blog(models.Model):
    """Класс для блога"""
    title = models.CharField(max_length=50, unique=True, verbose_name='наименование')
    content = models.TextField(verbose_name='содержимое', null=True, blank=True)
    preview = models.ImageField(upload_to="blog_photos/",verbose_name='превью', blank=True, null=True)
    publication = models.BooleanField(default=True, verbose_name='признак публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title} '

    class Meta:
        """Порядок сортировки по имени"""
        verbose_name = "<Блог>"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]
