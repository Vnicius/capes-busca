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
