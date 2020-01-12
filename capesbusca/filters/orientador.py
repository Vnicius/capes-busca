# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class Orientador(Filter):

    ''' Filtro do Orientador '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Orientador"
