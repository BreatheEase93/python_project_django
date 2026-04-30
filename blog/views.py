from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog


class BlogListView(ListView):
    """Список только опубликованных статей"""
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        # Фильтруем: только те, где publication=True
        return super().get_queryset().filter(publication=True)


class BlogDetailView(DetailView):
    """Просмотр статьи с увеличением счетчика"""
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    """Создание статьи"""
    model = Blog
    fields = ['title', 'content', 'preview', 'publication']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        # После создания переходим на просмотр статьи
        return reverse('blog:view', kwargs={'pk': self.object.pk})


class BlogUpdateView(UpdateView):
    """Редактирование статьи"""
    model = Blog
    fields = ['title', 'content', 'preview', 'publication']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        # После редактирования переходим на просмотр этой статьи
        return reverse('blog:view', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    """Удаление статьи"""
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:list')
