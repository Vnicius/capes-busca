# -*- coding: utf-8 -*-
from capesbusca.filters import Filter


class Autor(Filter):

    def __init__(self, value):
        super().__init__(value)

        self.campo = "Autor"
