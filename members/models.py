from django.db import models

# Create your models here.

class Membros(models.Model):

  nome = models.CharField(max_length=255)
  sobrenome = models.CharField(max_length=255)
  idade = models.IntegerField(default=0)
  numero = models.IntegerField(null=True)
  email = models.EmailField(max_length=255)
  dataEntrada = models.DateField(null=True)
  numeroMembro = models.IntegerField(null=True)
  categoria = models.CharField(max_length=255)
  vitorias = models.IntegerField(null=0, default=0)
  derrotas = models.IntegerField(null=0, default=0)
  desenpenho = models.CharField(null=True, max_length=255)

  def __str__(self):
    return f"{self.nome} {self.sobrenome}"