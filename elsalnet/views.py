from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Product
from .serializers import CompanySerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    filterset_fields = ['country']
    permission_classes = [IsAuthenticated]


class CompanyFilterView(APIView):
    search_fields = ['country']

    def post(self, request, format=None):
        country = request.data.get('country', None)

        # Провести фильтрацию объектов Suppliers по стране
        if country is not None:
            queryset = Company.objects.filter(country__icontains=country)
            serializer = CompanySerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Missing 'country' parameter"}, status=status.HTTP_400_BAD_REQUEST)
