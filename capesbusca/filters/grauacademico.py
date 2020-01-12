# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class GrauAcademico(Filter):

    ''' Filtro do Grau Acadêmico '''

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Grau Acadêmico"
