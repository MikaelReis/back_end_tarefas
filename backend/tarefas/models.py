from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
