
import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Products.models import Product
from Products.serializers import ProductSerializer


# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print("valid")
        return Response(serializer.data)
    return Response({"Invalid" : "not a valid serializer"}, status=400)