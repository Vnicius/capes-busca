# -*- coding: utf-8 -*-


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
