from .views import index , product_view , category_view
from django.urls import path
urlpatterns = [
    path('', index),
    path('products/<int:product_id>', product_view),
    path('categories/<int:category_id>/<str:category_slug>', category_view)
]

