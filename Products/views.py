from django.http import Http404
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from API.mixins import(
    StaffEditorPermissionMixin,
    UserQuerySetMixin
)
from API.authentication import TokenAuthentication
from API.permissions import IsStaffEditorPermission
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
product_detail_view = ProductDetailAPIView.as_view()



class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
product_list_view = ProductListAPIView.as_view()


# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
       
#         if content is None:
#             content=title
#         serializer.save(content=content)
        
# product_create_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [ authentication.SessionAuthentication, TokenAuthentication]
    # using custom permission
    #note the ordering of the permissions list
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    # #adding session authentication
    # # DjangoModelPermission, here only the super admin will be able to able to edit the model through the admin page but other staff  will list  (GET)products but cant create (POST, PUT) or send something to db
    # permission_classes = [permissions.DjangoModelPermissions]
    # #adding session authentication
    # # is authenticatedorreadonly will list  (GET)products but cant create (POST, PUT) or send something to db
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # #adding session authentication
    # # adding isauthenticated means the user must be authenticated
    # permission_classes = [permissions.IsAuthenticated]
     
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # email=serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
       
        if content is None:
            content=title
        serializer.save(user=self.request.user, content=content)
        
    # querying base on status of user
     # querying base on status of user 
    # this can also be done using the mixin method which is added to the view
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        print(request.user)
        return qs.filter(user=request.user)
    
product_list_create_view = ProductListCreateAPIView.as_view()


# using one function base view to perform crud
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method= request.method
    
    if method == 'GET':
        # urls args
        # get request -> detail view
        if pk is not None:
            # using get_object_or_404
            obj= get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        
            # # using queryset to filter it.
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404()
            # return Response(queryset)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        
    if method=='POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(user=self.request.user)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
        
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid" : "not a valid serializer"}, status=400)
    



# update api generic view
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        # return super().perform_update(serializer)
    
product_update_view = ProductUpdateAPIView.as_view()



# delete api generic view
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy (self, instance):
        super().perform_destroy(instance)
    
product_delete_view = ProductDestroyAPIView.as_view()


# using one generic view for crud operations
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        #print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content=" default content"
        serializer.save(content=content)
    
product_mixin_view = ProductMixinView.as_view()
 

# session authentication
# User & group permission with djangoModelPermissions