# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class Biblioteca(Filter):

    ''' Filtro da Biblioteca '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Biblioteca"
