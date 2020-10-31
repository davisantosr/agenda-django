from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
