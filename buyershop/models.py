from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('Название категории'),
        max_length=128,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name=_('URL')
    )
    created_date = models.DateTimeField(
        verbose_name=_('Дата создания категории'),
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        verbose_name=_('Дата изменения категории'),
        auto_now=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('Категория активна'),
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(
        verbose_name=_('Название продукта'),
        max_length=255,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name=_('URL')
    )
    cover = models.ImageField(
        verbose_name=_('Главное фото продукта'),
        upload_to='media/images',
    )
    price = models.DecimalField(
        verbose_name=_('Цена продукта'),
        decimal_places=2,
        max_digits=12
    )
    description = models.TextField(
        verbose_name=_('Описание продукта'),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_('Категория продукта'),
    )
    sex = models.CharField(
        max_length=125,
        choices=(
            ('Мужское', 'Мужское'),
            ('Женское', 'Женское'),
            ('Детское', 'Детское'),
            ('Унисекс', 'Унисекс')
        ),
        verbose_name='Пол'
    )
    created_date = models.DateTimeField(
        verbose_name=_('Дата создания продукта'),
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        verbose_name=_('Дата изменения продукта'),
        auto_now=True)
    is_active = models.BooleanField(
        verbose_name=_('Заказ активен'),
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    status = models.CharField(
        max_length=125,
        choices=(
            ('Выполнен', 'Выполнен'),
            ('Отклонен', 'Отклонен'),
            ('В ожидании', 'В ожидании'),
            ('До ожидании', 'До ожидании'),
        ),
        verbose_name='Статус заказа'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('Пользователь'),
    )
    created_date = models.DateTimeField(
        verbose_name=_('Дата создания заказа'),
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        verbose_name=_('Дата изменения заказа'),
        auto_now=True)
    is_active = models.BooleanField(
        verbose_name=_('Заказ активен'),
        default=True,
    )

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name=_('Продукт')
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='orderitems',
        verbose_name=_('Заказ')
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('Количество'),
        default=1,
        null=True,
        blank=True)
    created_date = models.DateTimeField(
        verbose_name=_('Дата создания заказа'),
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        verbose_name=_('Дата изменения заказа'),
        auto_now=True)
    is_active = models.BooleanField(
        verbose_name=_('Заказ активен'),
        default=True,
    )

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'


class DetailImage(models.Model):
    images = models.ImageField(
        verbose_name=_('Фотографии'),
        upload_to='media/images',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Продукты'),
        related_name='images'
    )

    class Meta:
        verbose_name = 'Детальная фотография'
        verbose_name_plural = 'Детальные фотографии'


class Worker(models.Model):
    name = models.CharField(
        verbose_name=_('Имя работника'),
        max_length=125,
    )
    image = models.ImageField(
        verbose_name=_('Фото сотрудника'),
        upload_to='media/images',
    )
    description = models.CharField(
        verbose_name=_('Описание сотрудника'),
        max_length=255,
    )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class OurService(models.Model):
    title = models.CharField(
        verbose_name=_('Название услуги'),
        max_length=125,
    )
    description = models.TextField(
        verbose_name=_('Описание услуги'),
    )

    class Meta:
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'


class Link(models.Model):
    link = models.URLField(
        verbose_name=_('Ссылка'),
        max_length=500
    )
    social_media = models.CharField(
        choices=(
            ('instagram', 'Инстаграм'),
            ('telegram', 'Телеграм'),
            ('whatsapp', 'Ватсап'),
            ('tiktok', 'Тик-ток')
        ),
        max_length=255
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
