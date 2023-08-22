from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    
    # thing that viewset comes with:
    
    # get -> list -> queryset
    # get-> retrieve -> detail view
    # post-> create -> new instance
    # put -> update instance
    # patch -> partial update instance
    # delete-> destroy
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    
class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    # get -> list -> queryset
    # get-> retrieve -> detail view
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
# product_list_view = ProductGenericViewSet.as_view({'get':'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})