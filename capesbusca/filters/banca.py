# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class Banca(Filter):

    ''' Filtro de Banca '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Banca"
