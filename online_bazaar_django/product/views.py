from django.db.models import Q
from django.http import Http404
from django.template.defaultfilters import slugify
from rest_framework.parsers import FormParser, MultiPartParser

from rest_framework import authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, catagory_slug):
        try: 
            return Category.objects.get(slug=catagory_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class GoodList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        goods = Product.objects.filter(seller=request.user)
        serializer = ProductSerializer(goods, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            try:
                product_slug = slugify(serializer.validated_data["name"])
                serializer.save(seller=request.user, slug=product_slug, image=request.FILES['image'])

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view( ['POST'] )
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else: 
        return Response({"products": []})

