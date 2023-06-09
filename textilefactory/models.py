from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class TextileOrderFile(models.Model):
    files = models.FileField(
        verbose_name=_('Файлы'),
        upload_to='media/files',
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class TextileOrder(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name=_('Название швейного заказа')
    )
    description = models.CharField(
        max_length=1024,
        verbose_name=_('Описание заказа')
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, _('Обрабатывается')),
            (2, _('Выполнен')),
        ),
        default=1,
        verbose_name=_('Статус заказа')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='textile_orders',
        verbose_name=_('Пользователь'),
    )
    created_date = models.DateTimeField(
        verbose_name=_('Дата создания швейного заказа'),
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        verbose_name=_('Дата изменения швейного заказа'),
        auto_now=True)
    is_active = models.BooleanField(
        verbose_name=_('Заказ активен'),
        default=True,
    )
    files = models.ForeignKey(TextileOrderFile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Швейный заказ {self.user}'

    class Meta:
        verbose_name = 'Швейный заказ'
        verbose_name_plural = 'Швейные заказы'


