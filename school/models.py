from django.conf import settings
from django.db import models
from django.utils.timezone import now

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    img = models.ImageField(upload_to='course/', **NULLABLE, verbose_name='превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='автор')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    title = models.CharField(max_length=150, verbose_name='название')
    img = models.ImageField(upload_to='lesson/img/', **NULLABLE, verbose_name='превью')
    video = models.URLField(**NULLABLE, verbose_name='видео')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='автор')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


TRANSFER = 'TR'
CASH = 'CH'

METHOD_CHOICES = [
    (TRANSFER, 'Перевод'),
    (CASH, 'Наличными'),
]


class Payments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    pay = models.PositiveIntegerField(**NULLABLE, verbose_name='сумма оплаты')
    date = models.DateTimeField(default=now, verbose_name='дата оплаты')
    method = models.CharField(default=TRANSFER, choices=METHOD_CHOICES, max_length=100, verbose_name='способ оплаты')
    sessions_url = models.CharField(**NULLABLE, verbose_name='URL')

    def __str__(self):
        return f'{self.user} : {self.course if self.course else self.lesson} - {self.pay}'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, related_name="subscription")
    is_active = models.BooleanField(default=True, verbose_name='подписка')

    def __str__(self):
        return f'{self.user} : {self.course} - {self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
