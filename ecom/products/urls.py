from django.contrib.auth import views
from django.conf.urls import url
from django.urls import path
from cart.views import add_to_cart, remove_from_cart, CartView, decreaseCart
from .views import ProductDetail, Home, update_product, upload, delete_product
from . import views
app_name = 'products'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload-product'),
    path('update/<int:product_id>', views.update_product),
    path('delete/<int:product_id>', views.delete_product),
    path('product/<slug>/',
         ProductDetail.as_view(), name='product'),
    url(r'^$', views.product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     views.product_list, name='product_list'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('', views.index, name='index'),

]
