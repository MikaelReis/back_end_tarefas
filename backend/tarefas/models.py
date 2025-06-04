from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    titulo = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    data_limite = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

