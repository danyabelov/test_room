from django.db import models
from users.models import User


class Room(models.Model):
    number = models.SmallIntegerField('Номер', unique=True, help_text='Номер комнаты')
    cost = models.DecimalField('Стоимость', default=0, help_text='Стоимость/сут.', decimal_places=2, max_digits=8)
    place_quantity = models.SmallIntegerField('Количество мест', default=1, help_text='Количество мест')

    class Meta:
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'

        def __str__(self):
            return f"Комната №{self.number}"


class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserved_user')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room', verbose_name='комната')
    start_date = models.DateField('Дата, ОТ',)
    end_date = models.DateField('Дата, ДО')

    class Meta:
        verbose_name = 'бронь'
        verbose_name_plural = 'брони'
