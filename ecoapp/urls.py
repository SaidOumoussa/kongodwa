from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('page/', views.index1, name='page'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('shoprod/', views.shoprod, name='shoprod'),
    path('base/', views.base, name='base'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product, name='product'),


    path('checkout/', views.checkout, name='checkout'),
    path('article/', views.article1, name='article'),
    path('shope/', views.shope, name='shope'),
    path('shop/', views.shop, name='shop'),
    path('shoping/', views.shoping, name='shoping'),

]
