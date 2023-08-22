from rest_framework.routers import DefaultRouter

from Products.viewset import ProductGenericViewSet

router = DefaultRouter()
router.register("product", ProductGenericViewSet, basename="products")

print(router.urls)
urlpatterns = router.urls

# from Products.viewset import ProductViewSet

# router = DefaultRouter()
# router.register("product", ProductViewSet, basename="products")

# print(router.urls)
# urlpatterns = router.urls