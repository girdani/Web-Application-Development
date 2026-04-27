from loja.models import *


class Fabricante(models.Model):
    # ------------------------------ FIELDS ------------------------------
    Fabricante = models.CharField(null=False, max_length=100)

    # ------------------------------ TIMESTAMPS -------------------------
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    
    # ------------------------------ MEETHODS ------------------------------
    def __str__(self):
        return '{}'.format(self. Fabricante)