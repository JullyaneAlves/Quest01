from django.db import models

# Create your models here.


from django.db import models

class Despesas(models.Model):
    Descricao = models.CharField(max_length=100)
    Data_criacao = models.DateField()
    Data_vencimento = models.DateField()
    Valor = models.FloatField()
    Tipo_despesa_choices = (('AL', 'Alimentação'),
                            ('MO', 'Moradia'),
                            ('CO', 'Combustível'),
                           )
    Tipo_despesa = models.CharField(max_length=2, choices=Tipo_despesa_choices)
    Forma_pagamento_choices = (('ES', 'Especie'),
                               ('BO', 'Boleto'),
                               ('CA', 'Cartão'),
                              )
    Forma_pagamento = models.CharField(max_length=2, choices=Forma_pagamento_choices)
    Quitado = models.BooleanField()
