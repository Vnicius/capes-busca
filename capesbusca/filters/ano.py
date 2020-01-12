# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class Ano(Filter):

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Ano"
