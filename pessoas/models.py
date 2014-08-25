from django.db import models

class Pessoa(models.Model):
	nome = models.CharField('Login',max_length=100)
	email = models.EmailField() 
	senha = models.CharField(max_length=15)
	ativo = models.BooleanField(default=True)
