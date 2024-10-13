from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, ProductViewSet, CompanyFilterView

# Создаем маршрутизатор и регистрируем наше представление
router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter/', CompanyFilterView.as_view(), name='filter_country'),
]