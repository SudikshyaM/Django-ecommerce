from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('products/',list),
    path('product/<int:product_id>/',product_detail,name='details'),
    path('addtocart/<int:product_id>/',add_to_cart,name='cart'),
    path('cart/',show_cart_items),
    path('delete<int:cart_id>/',delete_cart,name='delete'),
    path('orderform/<int:product_id>/<int:cart_id>/',order_form,name='order'),
    path('esewaform/',EsewaView.as_view(),name='esewaform'),
    path('esewaverify/<int:order_id>/<int:cart_id>/',esewa_verify),
    path('myorder/',my_order),
    path('details/<int:order_id>/',view_details),
]
