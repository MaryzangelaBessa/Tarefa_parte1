from django.db import models
from django.urls import reverse

class Evento(models.Model):
    TIPO_EVENTO_CHOICES = [
        (1, 'Congresso'),
        (2, 'Seminário'),
        (3, 'Workshop'),
        (4, 'Oficina'),
    ]
    titulo = models.CharField(verbose_name='Título',
                              max_length=50,
                              help_text='Informe o título do evento')
    data = models.DateField(verbose_name='Data')
    hora = models.TimeField(verbose_name='Hora')
    tipo = models.PositiveIntegerField(verbose_name='Tipo', choices=TIPO_EVENTO_CHOICES)
    local = models.CharField(verbose_name='Local',
                              max_length=150,
                              help_text='Informe o local do evento')
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-data']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        if self.pk:
            return reverse(self.detail_url, kwargs={'pk': self.pk})
        else:
            return reverse(self.list)

    @property
    def list_url(self):
        return 'evento:list'

    @property
    def edit_url(self):
        return 'evento:edit'

    @property
    def delete_url(self):
        return 'evento:delete'

    @property
    def detail_url(self):
        return 'evento:detail'