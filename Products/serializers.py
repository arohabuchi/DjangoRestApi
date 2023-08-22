from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import Product
from .  import validators 
from API.serializers import UserPublicSerializer




class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner =UserPublicSerializer(source="user",read_only=True)
    # related_products =ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True) 
    #serializer method of adding url
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field = "pk",
    )
    # email = serializers.EmailField(source="user.email", write_only=True)
    
    # adding custom validation method 2: validators.py
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            # 'email',
            'edit_url',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
            # 'my_discount',
            # 'my_user_data',
            # 'related_products',
        ]
        
        
        # gettin the user details
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }
    # #custom validation method 1
    # def validate_title(self, value):#validate_<fieldname>
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value) #iexact and exact are for case sensitivity
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists")
    #     return value.lower()
    
    
    
    ## to probably send email whenever an object is created
    # # note this can also be done in the create view
    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj
    
    # def update(self,instance, validated_data): #
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)
    
    
    # def get_url(self, obj):
    #     return f"/api/product/{obj.pk}/"
    
    # using reverse to get the url
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", request = request, kwargs={'pk': obj.pk})
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
