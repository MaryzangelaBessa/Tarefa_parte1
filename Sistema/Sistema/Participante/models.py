from django.db import models
from django.urls import reverse

class Participante(models.Model):
    STATUS_PARTICIPANTE_CHOICES = [
        (0, 'Não credenciado'),
        (1, 'Credenciado')
    ]
    nome = models.CharField(verbose_name='Nome', max_length=50, help_text='Informe o nome do participante')
    cpf = models.CharField(verbose_name='CPF', max_length=11, help_text='Informe o CPF do participante')
    email = models.EmailField(verbose_name='E-mail')
    rg = models.CharField(verbose_name='RG', max_length=11, help_text='Informe o RG do participante')
    status = models.PositiveIntegerField(verbose_name='Status', choices=STATUS_PARTICIPANTE_CHOICES)

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['nome']

    def get_absolute_url(self):
        if self.pk:
            return reverse(self.detail_url, kwargs={'pk': self.pk})
        else:
            return reverse(self.list)

    @property
    def list_url(self):
        return 'participante:list'

    @property
    def edit_url(self):
        return 'participante:edit'

    @property
    def delete_url(self):
        return 'participante:delete'

    @property
    def detail_url(self):
        return 'participante:detail'

    def __str__(self):
        return self.nome