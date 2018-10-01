from django.db import models
from django.urls import reverse

class Organizador(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50, help_text='Informe o nome do organizador')
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True, help_text='Informe o CPF do organizador')
    email = models.EmailField(verbose_name='E-mail')

    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'
        ordering = ['nome']

    def get_absolute_url(self):
        if self.pk:
            return reverse(self.detail_url, kwargs={'pk': self.pk})
        else:
            return reverse(self.list)

    @property
    def list_url(self):
        return 'organizador:list'

    @property
    def edit_url(self):
        return 'organizador:edit'

    @property
    def delete_url(self):
        return 'organizador:delete'

    @property
    def detail_url(self):
        return 'organizador:detail'

    def __str__(self):
        return self.nome