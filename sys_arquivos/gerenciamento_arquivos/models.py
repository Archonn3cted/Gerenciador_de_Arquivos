from django.db import models

class Bloco(models.Model):
    conteudo = models.CharField(max_length=1)
    ponteiro = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Bloco {self.id}: {self.conteudo} -> {self.ponteiro}'

class Arquivo(models.Model):
    nome = models.CharField(max_length=255)
    tamanho = models.IntegerField()
    endereco_inicial = models.ForeignKey(Bloco, on_delete=models.CASCADE)

    def __str__(self):
        return f'Arquivo {self.nome} ({self.tamanho} caracteres)'
