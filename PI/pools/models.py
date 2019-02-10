from django.db import models

# Create your models here.
class Questoes(object):
    def __init__(self, texto = '', data=''):
        self.texto = texto
        self.data = data