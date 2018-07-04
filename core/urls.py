from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('soporte/', views.soporte, name='soporte'),
    path('login/', views.login, name='login'),

]
