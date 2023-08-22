from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from  .models import Product

# #custom validation method 1
# def validate_title(value):#validate_<fieldname>
#     qs = Product.objects.filter(title__iexact=value) #iexact and exact are for case sensitivity
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} already exists")
#     return value.lower()


def validate_title_no_hello(value):

    if "shoe" in value:
        raise serializers.ValidationError("shoe not allowed.")
    return value.lower()

unique_product_title = UniqueValidator(queryset=Product.objects.all())