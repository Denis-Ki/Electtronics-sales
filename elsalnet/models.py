from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название продукта',
        help_text='введите название продукта'
    )
    model = models.CharField(
        max_length=50,
        verbose_name='Модель',
        **NULLABLE,
        help_text='введите название модели'
    )
    release_date = models.DateField(
        verbose_name='Дата выхода на рынок',
        **NULLABLE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Company(models.Model):
    FACTORY = 0
    RETAIL = 1
    ENTREPRENEUR = 2

    COMPANY_TYPES = [
        (FACTORY, 'Завод'),
        (RETAIL, 'Розничная сеть'),
        (ENTREPRENEUR, 'Индивидуальный предприниматель'),
    ]
    title = models.CharField(
        max_length=150,
        verbose_name='Название компании',
        help_text='введите название компании'
    )
    email = models.EmailField(
        verbose_name='email',
        help_text='введите e-mail'
    )
    country = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name='Страна',
        help_text='введите страну'
    )
    city = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name='Город',
        help_text='введите город'
    )
    street = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name='Улица',
        help_text='введите улицу'
    )
    house_number = models.CharField(
        max_length=20,
        **NULLABLE,
        verbose_name='Номер дома',
        help_text='введите номер дома'
    )
    products = models.ManyToManyField(
        Product,
        verbose_name='Продукты',
        help_text='выберите продукты'
    )
    supplier = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        **NULLABLE,
        limit_choices_to={'level__in': [0, 1]},
        verbose_name='Компания-поставщик',
        help_text='выберите компанию-поставщика, если Ваша компания не является заводом'
    )
    debt_to_supplier = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
        verbose_name='Задолженность',
        help_text='введите задолженность перед поставщиком'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    level = models.IntegerField(
        default=0,
        editable=False,
        verbose_name='Уровень'
    )
    company_type = models.IntegerField(
        choices=COMPANY_TYPES,
        default=FACTORY,
        editable=False,
        verbose_name='Тип компании'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец"
    )

    def save(self, *args, **kwargs):
        """Переопределение метода save() для обновления уровня при сохранении"""
        if self.supplier is None:
            # Узел нулевого уровня (завод)
            self.level = 0
            self.company_type = self.FACTORY
        elif self.supplier.level == 0:
            # Если поставщик на уровне 0 (завод), то это розничная сеть
            self.level = 1
            self.company_type = self.RETAIL
        elif self.supplier.level == 1:
            # Если поставщик на уровне 1 (розничная сеть), то это индивидуальный предприниматель
            self.level = 2
            self.company_type = self.ENTREPRENEUR
        else:
            raise ValidationError(f'Компания {self.supplier.title} не может являться поставщиком продукции')

    def clean(self):
        super().clean()
        if self.supplier and self.supplier.level not in [0, 1]:
            raise ValidationError({
                'supplier': 'Поставщик должен быть компанией с уровнем 0 или 1 (завод или розничная сеть).'
            })

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
