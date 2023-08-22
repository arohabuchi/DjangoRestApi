from django.urls import path

from . import views
urlpatterns = [
    path("", views.product_list_create_view, name="product-list"),
    # path("", views.product_list_create_view),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product-detail"),
    path("<int:pk>/update/", views.product_update_view, name="product-update"),
    path("<int:pk>/delete/", views.product_delete_view),
    
    
    
    # path("", views.product_list_create_view, name="product_list_create_view"),
    # # path("", views.product_create_view, name="product_create_view"),
    # path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail_view"),
]
