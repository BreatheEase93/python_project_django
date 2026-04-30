from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    # Главная со списком продуктов
    path('', views.ProductListView.as_view(), name='home'),

    # Страница контактов
    path('contacts/', views.FeedbackCreateView.as_view(), name='contacts'),

    # Детальная страница продукта
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # CRUD для продуктов
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    # CRUD для категорий
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
