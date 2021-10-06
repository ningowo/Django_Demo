from django.urls import path

from . import views

app_name='shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('<int:product_id>/add/', views.add, name='add'),
    path('<int:product_id>/remove/', views.remove, name='remove')
]