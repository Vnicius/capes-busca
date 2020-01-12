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

        ''' Classe para a construção da query de busca '''

        def __init__(self, term):
            '''
                Construtor da classe Builder

                Params:
                    term (str): termo da busca
            '''

            self.__search_query = SearchQuery()
            self.__search_query.term = term

        def build(self):
            '''
                Finaliza construção do objeto

                Returns:
                    (SearchResult): resultado da busca
            '''
            return self.__search_query

        def set_page(self, page):
            '''
                Define a página da busca

                Params:
                    page (int): número da página

                Returns:
                    (Builder): contrutor do SearchResult
            '''
            self.__search_query.page = page
            return self

        def set_page_size(self, page_size):
            '''
                Define o tamanho da página

                Params:
                    page_size (int): tamanho da página

                Returns:
                    (Builder): contrutor do SearchResult
            '''

            self.__search_query.page_size = page_size
            return self

        def add_filters(self, *args):
            '''
                Adiciona os filtros de busca

                Returns:
                    (Builder): contrutor do SearchResult
            '''

            for arg in args:
                self.__search_query.filters.append(vars(arg))

            return self
