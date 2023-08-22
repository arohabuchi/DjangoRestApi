from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# class UserProductInlineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk',
#         read_only=True
#     )
#     title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):#serializers.ModelSerializer
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    ###for ModelSerializer
    # class Meta:
    #     model = User
    #     fields = [
    #         'username',
    #         'id',
    #         'email',
    #     ]
    
    
    # other_product = serializers.SerializerMethodField(read_only=True)
    
    # def get_other_product(self, obj):
    #     # request = self.context.get('request')
    #     # print("this is user", obj)
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(my_products_qs, many=True, context=self.context).data