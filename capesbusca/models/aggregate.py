# -*- coding: utf-8 -*-


class Aggregate:

    ''' Modelo para os agregados '''

    def __init__(self, valor='', total=0):
        '''
            Construtor da classe Aggregate

            Attr:
                valor (str): valor do agregado
                total (int): total de trabalhos desse agregado
        '''

        self.valor = valor
        self.total = total

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        return str(vars(self))

    @staticmethod
    def parse(dictionary):
        '''
            Reliza o parser de dados em dict para o objeto

            Params:
                dictionary (dict): dicionário com os dados

            Returns:
                Aggregate
        '''

        valor = dictionary.get('valor', 0)
        total = dictionary.get('total', 0)

        return Aggregate(valor, total)
