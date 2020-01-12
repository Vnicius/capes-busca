# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class AreaConhecimento(Filter):

    ''' Filtro da Área de Conhecimento '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Área Conhecimento"
