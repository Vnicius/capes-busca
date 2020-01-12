# -*- coding: utf-8 -*-
from capesbusca.models.aggregate import Aggregate


class Aggregation:

    ''' Modelo para as agregações '''

    def __init__(self, campo='', total=0, agregados=[]):
        '''
            Construtor da classe Aggregation

            Attr:
                campo (str): nome da agregação
                total (int): total de agregados
                agregados (list): lista de agregados
        '''

        self.campo = campo
        self.total = total
        self.agregados = agregados

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))

    @staticmethod
    def parse(dictionary):

        campo = dictionary.get('campo', "")
        total = dictionary.get('total', "")
        agregados = []

        for agregado in dictionary.get('agregados', []):
            agregados.append(Aggregate().parse(agregado))

        return Aggregation(campo, total, agregados)
