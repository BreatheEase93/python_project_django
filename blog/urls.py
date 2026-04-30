from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', views.BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', views.BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)