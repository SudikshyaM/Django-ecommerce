from django.urls import path
from .views import *

urlpatterns = [
    path('',all_chai,name='all_chai'),
    path('store/',chaistore),
    path('product/',index),
    path('chais/',all_chai),
    path('<int:chai_id>/',desc,name='desc'),
    path('add/',post_product),
    path('update/<int:product_id>/',update,name='update'),
    path('delete/<int:product_id>/',delete,name='delete'),
    path('addcategory/',post_category,name='cat'),
    path('showCategory/',show_category),
    path('updatecat/<int:category_id>/',update_category,name='updatecat'),
    path('deletecat/<int:category_id>/',delete_category,name='deletecat')
]