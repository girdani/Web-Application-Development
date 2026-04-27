from loja.models import *


class Categoria(models.Model):
    # ------------------------------ FIELDS ------------------------------
    Categoria = models.CharField(null=False, max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    # ------------------------------ TIMESTAMPS -------------------------
    alterado_em = models.DateTimeField(auto_now=True)

    # ------------------------------ METHODS ------------------------------
    def __str__(self):
        return '{}'.format(self.Categoria)
