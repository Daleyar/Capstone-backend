from django.urls import path
from products import views 

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('cart/<int:buyer_id>/', views.ShoppingCart.as_view()),
]
