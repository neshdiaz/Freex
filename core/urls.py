from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('soporte/', views.soporte, name='soporte'),
    path('login/', views.login, name='login'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
