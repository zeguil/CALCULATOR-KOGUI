from django.db import models
from django.contrib.auth.models import User


class Operacao(models.Model):
    """
    representa uoperação matemática realizada por um usuário.
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    parametros = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username}: {self.parametros} = {self.resultado}'

    class Meta:
        ordering = ['-dt_inclusao']
        verbose_name_plural = "Operações"