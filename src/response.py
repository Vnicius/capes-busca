# -*- coding: utf-8 -*-
from src.models.work import Work
from src.models.aggregation import Aggregation


class Response:

    ''' 
        Classe para receber a reposta da requisição 
        e realizar o parser para os modelos
    '''

    def __init__(self, response_json):
        '''
            Construtor da classe Response

            Attr:
                response_json (dict): resposta da requisição
                page (int): número da página
                page_size (int): tamanho da página
                total (int): número total de trabalhos do resultado da requisição
                works (list): lista de trabalhos
                aggregations (list): lista de agregações
        '''
        self.response_json = response_json
        self.page = 0
        self.page_size = 0
        self.total = 0
        self.works = []
        self.aggregations = []

        self.__parse_response()

    def __parse_response(self):
        '''
            Realiza o parse da resposta da requisição para os modelos
        '''

        self.page = self.response_json.get('pagina', self.page)
        self.page_size = self.response_json.get(
            'registrosPorPagina', self.page_size)
        self.total = self.response_json.get('total', self.total)

        for work in self.response_json.get('tesesDissertacoes', self.works):
            self.works.append(Work().parse(work))

        for aggregation in self.response_json.get('agregacoes', self.aggregations):
            self.aggregations.append(Aggregation.parse(aggregation))
