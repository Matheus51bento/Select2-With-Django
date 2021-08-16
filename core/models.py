from django.db import models

# Create your models here.


class Comida(models.Model):
    descricao = models.CharField(max_length=200)
