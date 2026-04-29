from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns=[
    path("contacts/", views.contacts, name="contacts"),
    path("home/", views.home, name="home"),
    path("", views.index, name="index"),
    path("product/<int:pk>/", views.show_product, name="product"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
