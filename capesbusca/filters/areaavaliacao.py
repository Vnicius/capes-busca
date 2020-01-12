# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class AreaAvaliacao(Filter):

    ''' Filtro da Área de Avaliação '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Área Avaliação"
