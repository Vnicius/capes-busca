# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class Instituicao(Filter):

    ''' Filtro da Instituição '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Instituição"
