from django.test import TestCase
from django.contrib.auth import get_user_model
from elsalnet.models import Product, Company

User = get_user_model()


class ProductModelTest(TestCase):

    def setUp(self):
        """Создание тестового продукта"""
        self.product = Product.objects.create(
            title="Тестовый продукт",
            model="Модель A",
            release_date="2022-01-01"
        )

    def test_product_creation(self):
        """Проверка создания продукта"""
        self.assertEqual(self.product.title, "Тестовый продукт")
        self.assertEqual(self.product.model, "Модель A")
        self.assertEqual(str(self.product.release_date), "2022-01-01")

    def test_product_string_representation(self):
        """Проверка строкового представления продукта"""
        self.assertEqual(str(self.product), "Тестовый продукт")


class CompanyModelTest(TestCase):

    def setUp(self):
        """Создание пользователей и компаний для тестирования"""
        self.user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="password123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="password456"
        )
        self.factory = Company.objects.create(
            title="Завод A",
            email="factory@example.com",
            country="Россия",
            city="Москва",
            street="Ленина",
            house_number="1",
            debt_to_supplier=0.00,
            owner=self.user1
        )
        self.retail_network = Company.objects.create(
            title="Розничная сеть B",
            email="retail@example.com",
            country="Россия",
            city="Санкт-Петербург",
            street="Пушкина",
            house_number="2",
            debt_to_supplier=50000.00,
            supplier=self.factory,
            owner=self.user2
        )

    def test_company_creation(self):
        """Проверка создания компании и расчета уровня"""
        self.assertEqual(self.factory.title, "Завод A")
        self.assertEqual(self.factory.level, 0)  # Завод — 0 уровень
        self.assertEqual(self.retail_network.level, 1)  # Розничная сеть — 1 уровень

    def test_company_debt(self):
        """Проверка задолженности перед поставщиком"""
        self.assertEqual(self.retail_network.debt_to_supplier, 50000.00)

    def test_supplier_relationship(self):
        """Проверка связки поставщика"""
        self.assertEqual(self.retail_network.supplier, self.factory)

    def test_company_string_representation(self):
        """Проверка строкового представления компании"""
        self.assertEqual(str(self.factory), "Завод A")
        self.assertEqual(str(self.retail_network), "Розничная сеть B")