from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='news'),
    path('news/', views.news, name='news'),
    path('products/', views.prod, name='products'),
    path('products/<int:product_id>', views.prod_details, name='product_details'),
    path('services/', views.serv, name='services'),
    path('services/<int:service_id>', views.serv_details, name='service_details'),
    path('about/', views.abt, name='about'),
    path('contact/', views.cont, name='contact'),
]