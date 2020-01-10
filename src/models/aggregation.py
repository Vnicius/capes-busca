# -*- coding: utf-8 -*-
from src.models.aggregate import Aggregate


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

    @staticmethod
    def parse(dictionary):

        campo = dictionary.get('campo', "")
        total = dictionary.get('total', "")
        agregados = []

        for agregado in dictionary.get('agregados', []):
            agregados.append(Aggregate().parse(agregado))

        return Aggregation(campo, total, agregados)
