# -*- coding: utf-8 -*-
from capesbusca.models import Work, Aggregation


class SearchResult:

    ''' 
        Classe para receber a reposta da requisição 
        e realizar o parser para os modelos
    '''

    def __init__(self, result_json):
        '''
            Construtor da classe Response

            Attr:
                result_json (dict): resposta da requisição
                page (int): número da página
                page_size (int): tamanho da página
                total (int): número total de trabalhos do resultado da requisição
                works (list): lista de trabalhos
                aggregations (list): lista de agregações
        '''
        self.result_json = result_json
        self.page = 0
        self.page_size = 0
        self.total = 0
        self.works = []
        self.aggregations = []

        self.__parse_json()

    def __repr__(self):
        data_dict = vars(self)
        data_dict.pop('result_json')

        return str(vars(self))

    def __str__(self):
        data_dict = vars(self)
        data_dict.pop('result_json')

        return str(vars(self))

    def __parse_json(self):
        '''
            Realiza o parse da resposta da requisição para os modelos
        '''

        self.page = self.result_json.get('pagina', self.page)
        self.page_size = self.result_json.get(
            'registrosPorPagina', self.page_size)
        self.total = self.result_json.get('total', self.total)

        for work in self.result_json.get('tesesDissertacoes', self.works):
            self.works.append(Work().parse(work))

        for aggregation in self.result_json.get('agregacoes', self.aggregations):
            self.aggregations.append(Aggregation.parse(aggregation))
