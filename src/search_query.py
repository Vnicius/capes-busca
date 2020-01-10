# -*- coding: utf-8 -*-
from json import dumps


class SearchQuery:

    ''' Classe para construir a query de busca '''

    def __init__(self, term="", filters=[], page=1, page_size=20):
        '''
            Construtor da classe SearchQuery

            Attr:
                term (str): termo da busca
                filters (array): filtros da busca
                page (int): página
                page_size (int): tamanho da página
        '''

        self.term = term
        self.filters = filters
        self.page = page
        self.page_size = page_size

    def json(self):
        '''
            Cria o JSON da busca
        '''

        return dumps({"termo": self.term,
                      "filtros": self.filters,
                      "pagina": self.page,
                      "registrosPorPagina": self.page_size})
