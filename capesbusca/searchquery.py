# -*- coding: utf-8 -*-
from json import dumps


class SearchQuery:

    ''' Classe para construir a query de busca '''

    def __init__(self):
        '''
            Construtor da classe SearchQuery

            Attr:
                term (str): termo da busca
                filters (array): filtros da busca
                page (int): página
                page_size (int): tamanho da página
        '''

        self.term = ""
        self.filters = []
        self.page = 1
        self.page_size = 20

    def json(self):
        '''	
            Cria o JSON da busca	
        '''

        return dumps({"termo": self.term,
                      "filtros": self.filters,
                      "pagina": self.page,
                      "registrosPorPagina": self.page_size})

    class Builder:

        def __init__(self, term):
            self.__search_query = SearchQuery()
            self.__search_query.term = term

        def build(self):
            return self.__search_query

        def set_page(self, page):
            self.__search_query.page = page
            return self

        def set_page_size(self, page_size):
            self.__search_query.page_size = page_size
            return self

        def add_filters(self, *args):
            for arg in args:
                self.__search_query.filters.append(vars(arg))

            return self
